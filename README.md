# Notification Test Suite

![CI](https://github.com/uriel-P-V/notification-test-suite/actions/workflows/tests.yml/badge.svg)

A contract-based test suite for a notification and alerting system —
demonstrates contract testing, dependency injection, and mock-based
testing for email, SMS, and push notifications.

---

## Project Structure

```
notification-test-suite/
├── notifier/
│   ├── __init__.py
│   ├── contracts.py              ← Data contracts and validation
│   └── notification_service.py  ← Notification and alert service
├── tests/
│   ├── conftest.py               ← Shared fixtures
│   ├── test_contracts.py         ← 6 contract validation tests
│   ├── test_notifications.py     ← 6 functional tests
│   └── test_alerts.py            ← 4 alert tests
├── .github/
│   └── workflows/
│       └── tests.yml             ← GitHub Actions CI
├── pytest.ini
└── requirements.txt
```

---

## Features

- **Contract testing** — validates data structure compliance
- **Dependency injection** — mockable external sender
- **16 automated tests** — contracts, notifications, alerts
- **GitHub Actions CI** — runs on every push with coverage reporting

---

## Contract Testing

```python
# Define the contract
NOTIFICATION_CONTRACT = {
    "id":        str,
    "type":      str,
    "recipient": str,
    "message":   str,
    "status":    str,
    "timestamp": float,
}

# Validate any data against the contract
violations = validate_contract(data, NOTIFICATION_CONTRACT)
assert violations == []  # no violations = contract fulfilled
```

---

## Setup

```bash
git clone https://github.com/uriel-P-V/notification-test-suite.git
cd notification-test-suite
pip install -r requirements.txt
pytest tests/ -v
```

---

## Running Tests

```bash
# All tests
pytest

# With coverage
pytest --cov=notifier --cov-report=term-missing

# By marker
pytest -m contract
pytest -m smoke
```

---

## Tech Stack

- **Python 3.10+**
- **unittest.mock** — MagicMock, dependency injection
- **Pytest** — fixtures, markers, parametrize
- **GitHub Actions** — CI/CD pipeline

---

## Author

**Uriel Alejandro Pérez Valdovinos**  
[github.com/uriel-P-V](https://github.com/uriel-P-V) · [linkedin.com/in/uriel-pv](https://linkedin.com/in/uriel-pv)