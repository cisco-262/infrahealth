from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional


@dataclass
class CheckResult:
    check: str
    target: str
    status: str
    ok: bool
    latency_ms: Optional[float] = None
    detail: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
