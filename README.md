# InfraHealth

A lightweight Python CLI for checking host reachability, TCP ports, and HTTP/HTTPS service health.

InfraHealth is designed for small infrastructure checks, homelabs, lab environments, and simple operational verification without requiring a monitoring server or database.

## Features

- Ping reachability checks
- TCP port checks
- HTTP/HTTPS availability checks
- Response-time measurement
- Console summary
- JSON report export
- Simple JSON configuration
- Cross-platform Python structure

## Requirements

- Python 3.10+
- `requests`

Ping behavior depends on the operating system's built-in `ping` command.

## Quick Start

Clone the repository and install dependencies:

```bash
git clone https://github.com/cisco-262/infrahealth.git
cd infrahealth
python -m venv .venv
```

Activate the virtual environment.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run InfraHealth:

```bash
python main.py
```

Use a custom configuration:

```bash
python main.py --config my-config.json
```

Run without creating a JSON report:

```bash
python main.py --no-json
```

## Configuration

Example:

```json
{
  "targets": [
    {
      "name": "Website",
      "host": "example.com",
      "ping": true,
      "ports": [80, 443],
      "urls": [
        "https://example.com"
      ]
    },
    {
      "name": "Linux Server",
      "host": "192.168.1.20",
      "ping": true,
      "ports": [22, 80, 443]
    }
  ]
}
```

### Target fields

| Field | Required | Description |
|---|---:|---|
| `name` | No | Friendly display name |
| `host` | Yes | Hostname or IP address |
| `ping` | No | Enable ICMP ping |
| `ports` | No | List of TCP ports |
| `urls` | No | HTTP or HTTPS URLs |

## Example Output

```text
InfraHealth v0.1.0
────────────────────────────────────────────────

OpsHome
  Ping                     ✓ ONLINE        35 ms
  TCP 80                   ✓ OPEN          42 ms
  TCP 443                  ✓ OPEN          39 ms
  https://opshome.run      ✓ HTTP 200     181 ms

────────────────────────────────────────────────
Targets 1 | Healthy 1 | Warning 0 | Failed 0

JSON report: reports/report-20260817-181000.json
```

## Health Classification

InfraHealth currently uses a deliberately simple target-level classification:

- **Healthy** — all configured checks succeed.
- **Warning** — at least one check succeeds and at least one fails.
- **Failed** — all configured checks fail.

This behavior may become configurable in later releases.

## Development

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run tests:

```bash
pytest
```

## Roadmap

### v0.1.0
- Ping
- TCP port checks
- HTTP/HTTPS checks
- Console and JSON reports

### v0.2.0
- DNS checks
- TLS certificate inspection

### v0.3.0
- CSV/HTML reports
- Historical results

### v0.4.0
- Scheduled checks
- Alert integrations

## Project Goals

InfraHealth intentionally starts small. It is not intended to replace full monitoring platforms such as Prometheus, Zabbix, or enterprise observability products.

The goal is to provide a simple command-line health checker that is easy to understand, easy to run, and easy to extend.

## Security

InfraHealth performs outbound connectivity and availability checks only. It does not authenticate to remote systems, execute remote commands, or perform vulnerability scanning.

## License

MIT License.
