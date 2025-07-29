import socket
import json
import psutil
import requests
from fireguard_scout.utils import get_ip_addresses

def collect_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "mem_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
    }

def send_report(data):
    try:
        response = requests.post("http://localhost:8080/api/status", json=data)
        print("Response:", response.status_code, response.text)
    except Exception as e:
        print("Error sending data:", e)

from datetime import datetime, timezone


def main():
    hostname = socket.gethostname()
    metrics = collect_metrics()

    payload = {
        "hostname": hostname,
        "location": "unknown",  # placeholder for future enhancement
        "services": {
            "cpu": f"{metrics['cpu_percent']}%",
            "memory": f"{metrics['mem_percent']}%",
            "disk": f"{metrics['disk_percent']}%"
        },
        "interfaces": get_ip_addresses(),  # ← New addition
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    print(f"[SCOUT] Reporting in: {json.dumps(payload, indent=2)}")
    send_report(payload)
