import pytest
from notifier.contracts import (
    NOTIFICATION_CONTRACT,
    ALERT_CONTRACT,
    validate_contract,
)


def test_valid_notification_passes_contract(sample_notification):
    violations = validate_contract(sample_notification, NOTIFICATION_CONTRACT)
    assert violations == []


def test_missing_field_detected(sample_notification):
    data = sample_notification.copy()
    del data["recipient"]
    violations = validate_contract(data, NOTIFICATION_CONTRACT)
    assert "Missing required field: 'recipient'" in violations


def test_wrong_type_detected(sample_notification):
    data = sample_notification.copy()
    data["timestamp"] = "not a float"
    violations = validate_contract(data, NOTIFICATION_CONTRACT)
    assert "Field 'timestamp' expected float but got str" in violations


def test_valid_alert_passes_contract(sample_alert):
    violations = validate_contract(sample_alert, ALERT_CONTRACT)
    assert violations == []


def test_alert_missing_field_detected(sample_alert):
    data = sample_alert.copy()
    del data["source"]
    violations = validate_contract(data, ALERT_CONTRACT)
    assert "Missing required field: 'source'" in violations


def test_multiple_violations_detected(sample_notification):
    data = sample_notification.copy()
    del data["recipient"]
    data["timestamp"] = "not a float"
    violations = validate_contract(data, NOTIFICATION_CONTRACT)
    assert len(violations) == 2
    assert "Missing required field: 'recipient'" in violations
    assert "Field 'timestamp' expected float but got str" in violations