import argparse
import json
import sys
from pathlib import Path

from infrahealth.reporter import print_console, save_json
from infrahealth.runner import run_all


def load_config(path: str):
    config_path = Path(path)

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as handle:
        config = json.load(handle)

    targets = config.get("targets")
    if not isinstance(targets, list) or not targets:
        raise ValueError("Config must contain a non-empty 'targets' list.")

    for index, target in enumerate(targets, start=1):
        if "host" not in target:
            raise ValueError(f"Target #{index} is missing required field 'host'.")

    return config


def parse_args():
    parser = argparse.ArgumentParser(
        description="Lightweight infrastructure health checks from your terminal."
    )
    parser.add_argument(
        "-c",
        "--config",
        default="examples/config.example.json",
        help="Path to the JSON configuration file.",
    )
    parser.add_argument(
        "--no-json",
        action="store_true",
        help="Do not save a JSON report.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        config = load_config(args.config)
        results = run_all(config)
        print_console(results)

        if not args.no_json:
            report = save_json(results)
            print(f"\nJSON report: {report}")

        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
