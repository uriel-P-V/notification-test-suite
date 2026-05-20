import pytest
from unittest.mock import MagicMock
from notifier import NotificationService


@pytest.fixture
def service():
    """NotificationService without external sender."""
    return NotificationService()


@pytest.fixture
def mock_sender():
    """Fake external email/SMS sender."""
    return MagicMock()


@pytest.fixture
def service_with_sender(mock_sender):
    """NotificationService with mocked sender."""
    return NotificationService(sender=mock_sender)


@pytest.fixture
def sample_notification():
    """Sample valid notification data."""
    return {
        "id":        "notif-001",
        "type":      "email",
        "recipient": "uriel@example.com",
        "message":   "Your storage volume is at 90% capacity",
        "status":    "sent",
        "timestamp": 1234567890.0,
    }


@pytest.fixture
def sample_alert():
    """Sample valid alert data."""
    return {
        "alert_id":  "alert-001",
        "level":     "warning",
        "message":   "Disk usage above 80%",
        "source":    "storage-monitor",
        "timestamp": 1234567890.0,
        "resolved":  False,
    }