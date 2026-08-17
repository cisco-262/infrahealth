import socket
import time
from .models import CheckResult


def check_tcp(host: str, port: int, timeout: int = 3) -> CheckResult:
    started = time.perf_counter()

    try:
        with socket.create_connection((host, port), timeout=timeout):
            latency = (time.perf_counter() - started) * 1000
            return CheckResult(
                check=f"tcp:{port}",
                target=host,
                status="OPEN",
                ok=True,
                latency_ms=round(latency, 2),
            )
    except socket.timeout:
        return CheckResult(
            check=f"tcp:{port}",
            target=host,
            status="TIMEOUT",
            ok=False,
        )
    except OSError as exc:
        return CheckResult(
            check=f"tcp:{port}",
            target=host,
            status="CLOSED",
            ok=False,
            detail=str(exc),
        )
