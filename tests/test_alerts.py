
import pytest

from notifier.contracts import ALERT_CONTRACT, validate_contract


def test_send_alert_valid_contract(service_with_sender, sample_alert):
    service = service_with_sender

    result = service.send_alert(
        level=sample_alert["level"],
        message=sample_alert["message"],
        source=sample_alert["source"],
    )

    violations = validate_contract(result, ALERT_CONTRACT)
    assert violations == []

def test_send_critical_alert(service_with_sender, sample_alert):
    service = service_with_sender

    result = service.send_alert(
        level="critical",
        message=sample_alert["message"],
        source=sample_alert["source"],
    )

    assert result["level"] == "critical"

def test_send_invalid_level_raises_error(service_with_sender, sample_alert):
    service = service_with_sender

    with pytest.raises(ValueError) as exc_info:
        service.send_alert(
            level="invalid_level",
            message=sample_alert["message"],
            source=sample_alert["source"],
        )
    assert "Invalid level 'invalid_level'" in str(exc_info.value)

def test_alert_resolved_is_false_by_default(service_with_sender, sample_alert):
    service = service_with_sender

    result = service.send_alert(
        level=sample_alert["level"],
        message=sample_alert["message"],
        source=sample_alert["source"],
    )

    assert result["resolved"] is False
