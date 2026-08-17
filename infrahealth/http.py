import time
import requests
from .models import CheckResult


def check_http(url: str, timeout: int = 5) -> CheckResult:
    started = time.perf_counter()

    try:
        response = requests.get(
            url,
            timeout=timeout,
            allow_redirects=True,
            headers={"User-Agent": "InfraHealth/0.1.0"},
        )
        latency = (time.perf_counter() - started) * 1000
        ok = 200 <= response.status_code < 400

        return CheckResult(
            check="http",
            target=url,
            status=f"HTTP {response.status_code}",
            ok=ok,
            latency_ms=round(latency, 2),
            detail=str(response.url) if response.url != url else None,
        )
    except requests.RequestException as exc:
        return CheckResult(
            check="http",
            target=url,
            status="ERROR",
            ok=False,
            detail=str(exc),
        )
