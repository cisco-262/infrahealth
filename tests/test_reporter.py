from infrahealth.models import CheckResult
from infrahealth.reporter import summarize


def test_summary():
    results = {
        "healthy": [
            CheckResult("ping", "a", "ONLINE", True),
            CheckResult("tcp:443", "a", "OPEN", True),
        ],
        "warning": [
            CheckResult("ping", "b", "ONLINE", True),
            CheckResult("tcp:443", "b", "CLOSED", False),
        ],
        "failed": [
            CheckResult("ping", "c", "UNREACHABLE", False),
        ],
    }

    assert summarize(results) == {
        "targets": 3,
        "healthy": 1,
        "warning": 1,
        "failed": 1,
    }
