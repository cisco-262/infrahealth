from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Dict, List

from .models import CheckResult


def summarize(results: Dict[str, List[CheckResult]]) -> Dict[str, int]:
    targets = len(results)
    healthy = 0
    warning = 0
    failed = 0

    for checks in results.values():
        if checks and all(item.ok for item in checks):
            healthy += 1
        elif checks and any(item.ok for item in checks):
            warning += 1
        else:
            failed += 1

    return {
        "targets": targets,
        "healthy": healthy,
        "warning": warning,
        "failed": failed,
    }


def print_console(results: Dict[str, List[CheckResult]]) -> None:
    print("\nInfraHealth v0.1.0")
    print("─" * 48)

    for name, checks in results.items():
        print(f"\n{name}")

        for item in checks:
            icon = "✓" if item.ok else "✗"
            latency = (
                f"  {item.latency_ms:.0f} ms"
                if item.latency_ms is not None
                else ""
            )
            detail = f"  ({item.detail})" if item.detail else ""

            if item.check == "ping":
                label = "Ping"
            elif item.check.startswith("tcp:"):
                label = f"TCP {item.check.split(':', 1)[1]}"
            else:
                label = item.target

            print(f"  {label:<24} {icon} {item.status:<12}{latency}{detail}")

    stats = summarize(results)
    print("\n" + "─" * 48)
    print(
        f"Targets {stats['targets']} | "
        f"Healthy {stats['healthy']} | "
        f"Warning {stats['warning']} | "
        f"Failed {stats['failed']}"
    )


def save_json(
    results: Dict[str, List[CheckResult]],
    output_dir: str = "reports",
) -> Path:
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = path / f"report-{timestamp}.json"

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "version": "0.1.0",
        "summary": summarize(results),
        "targets": {
            name: [item.to_dict() for item in checks]
            for name, checks in results.items()
        },
    }

    output_file.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return output_file
