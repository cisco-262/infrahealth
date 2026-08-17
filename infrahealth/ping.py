import platform
import re
import subprocess
from .models import CheckResult


def check_ping(host: str, timeout: int = 2) -> CheckResult:
    system = platform.system().lower()

    if system == "windows":
        command = ["ping", "-n", "1", "-w", str(timeout * 1000), host]
    else:
        command = ["ping", "-c", "1", "-W", str(timeout), host]

    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout + 2,
            check=False,
        )
    except (subprocess.TimeoutExpired, OSError) as exc:
        return CheckResult(
            check="ping",
            target=host,
            status="ERROR",
            ok=False,
            detail=str(exc),
        )

    output = f"{completed.stdout}\n{completed.stderr}"

    if completed.returncode != 0:
        return CheckResult(
            check="ping",
            target=host,
            status="UNREACHABLE",
            ok=False,
        )

    latency = None
    patterns = [
        r"time[=<]?\s*(\d+(?:\.\d+)?)\s*ms",
        r"Average = (\d+)ms",
    ]
    for pattern in patterns:
        match = re.search(pattern, output, re.IGNORECASE)
        if match:
            latency = float(match.group(1))
            break

    return CheckResult(
        check="ping",
        target=host,
        status="ONLINE",
        ok=True,
        latency_ms=latency,
    )
