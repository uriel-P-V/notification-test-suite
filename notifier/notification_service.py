"""
notification_service.py
-----------------------
Simulates a notification service that sends emails, SMS, and push notifications.
Uses dependency injection for the sender — making it easily mockable in tests.
"""

import time
import uuid
from .contracts import (
    VALID_NOTIFICATION_TYPES,
    VALID_ALERT_LEVELS,
    NOTIFICATION_CONTRACT,
    ALERT_CONTRACT,
    validate_contract
)


class NotificationError(Exception):
    """Raised when a notification cannot be sent."""
    pass


class NotificationService:

    def __init__(self, sender=None):
        """
        Args:
            sender: External sender dependency (email/SMS client).
                    If None uses a default mock-friendly sender.
        """
        self._sender = sender
        self._sent = []

    def send(self, notification_type: str, recipient: str, message: str) -> dict:
        """
        Send a notification.

        Args:
            notification_type: "email", "sms", or "push"
            recipient:         Email address or phone number
            message:           Notification content

        Returns:
            dict matching NOTIFICATION_CONTRACT
        """
        if notification_type not in VALID_NOTIFICATION_TYPES:
            raise ValueError(
                f"Invalid type '{notification_type}'. "
                f"Must be one of {VALID_NOTIFICATION_TYPES}"
            )
        if not recipient or not message:
            raise ValueError("recipient and message are required")

        # Try to send via external sender
        status = "sent"
        try:
            if self._sender:
                self._sender.send(recipient, message)
        except Exception as e:
            status = "failed"

        notification = {
            "id":        str(uuid.uuid4()),
            "type":      notification_type,
            "recipient": recipient,
            "message":   message,
            "status":    status,
            "timestamp": time.time(),
        }

        self._sent.append(notification)
        return notification

    def send_alert(self, level: str, message: str, source: str) -> dict:
        """
        Send a system alert.

        Args:
            level:   "info", "warning", or "critical"
            message: Alert description
            source:  System that triggered the alert
        """
        if level not in VALID_ALERT_LEVELS:
            raise ValueError(f"Invalid level '{level}'")
        if not message or not source:
            raise ValueError("message and source are required")

        alert = {
            "alert_id":  str(uuid.uuid4()),
            "level":     level,
            "message":   message,
            "source":    source,
            "timestamp": time.time(),
            "resolved":  False,
        }
        return alert

    def get_sent(self) -> list:
        """Return all sent notifications."""
        return self._sent.copy()

    def get_sent_count(self, status: str = None) -> int:
        """Count sent notifications, optionally filtered by status."""
        if status:
            return sum(1 for n in self._sent if n["status"] == status)
        return len(self._sent)