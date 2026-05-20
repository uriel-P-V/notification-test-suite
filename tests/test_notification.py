import pytest
from notifier.contracts import NOTIFICATION_CONTRACT, validate_contract


def test_send_email_returns_valid_notification(service_with_sender, sample_notification):
    service = service_with_sender
    service._sender.send.return_value = None

    result = service.send(
        notification_type=sample_notification["type"],
        recipient=sample_notification["recipient"],
        message=sample_notification["message"],
    )

    violations = validate_contract(result, NOTIFICATION_CONTRACT)
    assert violations == []


def test_send_sms_status_is_sent(service_with_sender, sample_notification):
    service = service_with_sender
    service._sender.send.return_value = None

    result = service.send(
        notification_type="sms",
        recipient=sample_notification["recipient"],
        message=sample_notification["message"],
    )

    assert result["status"] == "sent"


def test_send_invalid_type_raises_error(service_with_sender, sample_notification):
    service = service_with_sender

    with pytest.raises(ValueError) as exc_info:
        service.send(
            notification_type="invalid_type",
            recipient=sample_notification["recipient"],
            message=sample_notification["message"],
        )
    assert "Invalid type 'invalid_type'" in str(exc_info.value)


def test_send_empty_recipient_raises_error(service_with_sender, sample_notification):
    service = service_with_sender

    with pytest.raises(ValueError) as exc_info:
        service.send(
            notification_type=sample_notification["type"],
            recipient="",
            message=sample_notification["message"],
        )
    assert "recipient and message are required" in str(exc_info.value)


def test_sender_called_with_correct_params(service_with_sender, sample_notification):
    service = service_with_sender
    service._sender.send.return_value = None

    service.send(
        notification_type=sample_notification["type"],
        recipient=sample_notification["recipient"],
        message=sample_notification["message"],
    )

    service._sender.send.assert_called_once_with(
        sample_notification["recipient"],
        sample_notification["message"]
    )


def test_get_sent_count(service_with_sender, sample_notification):
    service = service_with_sender
    service._sender.send.return_value = None

    for _ in range(3):
        service.send(
            notification_type=sample_notification["type"],
            recipient=sample_notification["recipient"],
            message=sample_notification["message"],
        )

    assert service.get_sent_count() == 3