"""
contracts.py
------------
Defines the data contracts for the notification system.
Contract testing ensures that any change to the data structure
is detected immediately before reaching production.
"""

# Valid values for each field
VALID_NOTIFICATION_TYPES = {"email", "sms", "push"}
VALID_NOTIFICATION_STATUSES = {"sent", "failed", "pending"}

# The notification contract — defines required fields and types
NOTIFICATION_CONTRACT = {
    "id":        str,
    "type":      str,
    "recipient": str,
    "message":   str,
    "status":    str,
    "timestamp": float,
}

# Alert contract — for system alerts
ALERT_CONTRACT = {
    "alert_id":  str,
    "level":     str,    # "info", "warning", "critical"
    "message":   str,
    "source":    str,
    "timestamp": float,
    "resolved":  bool,
}

VALID_ALERT_LEVELS = {"info", "warning", "critical"}


def validate_contract(data: dict, contract: dict) -> list:
    """
    Validates that data matches a contract.

    Returns:
        List of violation messages. Empty list means valid.
    """
    violations = []

    for field, expected_type in contract.items():
        if field not in data:
            violations.append(f"Missing required field: '{field}'")
        elif not isinstance(data[field], expected_type):
            actual_type = type(data[field]).__name__
            violations.append(
                f"Field '{field}' expected {expected_type.__name__} "
                f"but got {actual_type}"
            )

    return violations