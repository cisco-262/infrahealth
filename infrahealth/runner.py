from typing import Any, Dict, List

from .http import check_http
from .models import CheckResult
from .ping import check_ping
from .tcp import check_tcp


def run_target(target: Dict[str, Any]) -> List[CheckResult]:
    results: List[CheckResult] = []
    host = target["host"]

    if target.get("ping", False):
        results.append(check_ping(host))

    for port in target.get("ports", []):
        results.append(check_tcp(host, int(port)))

    for url in target.get("urls", []):
        results.append(check_http(url))

    return results


def run_all(config: Dict[str, Any]) -> Dict[str, List[CheckResult]]:
    output: Dict[str, List[CheckResult]] = {}

    for target in config.get("targets", []):
        name = target.get("name") or target["host"]
        output[name] = run_target(target)

    return output
