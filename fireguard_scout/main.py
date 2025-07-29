import json
import socket
import requests
from datetime import datetime, timezone
from fireguard_scout.utils import get_ip_addresses, get_os_info
from fireguard_scout.metrics import get_metrics  # assumed to return cpu/mem/disk dict

FIREGUARD_URL = "http://localhost:8080/api/status"  # 🔁 Update as needed

def send_payload():
    hostname = socket.gethostname()
    metrics = get_metrics()
    ip_data = get_ip_addresses()
    os_info = get_os_info()

    payload = {
        "hostname": hostname,
        "location": "unknown",  # Optionally set this later
        "services": {
            "cpu": f"{metrics['cpu_percent']}%",
            "memory": f"{metrics['mem_percent']}%",
            "disk": f"{metrics['disk_percent']}%"
        },
        "interfaces": ip_data,
        "system_info": os_info,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    try:
        response = requests.post(FIREGUARD_URL, json=payload, timeout=5)
        response.raise_for_status()
        print(f"[+] Payload sent successfully: {response.status_code}")
    except requests.RequestException as e:
        print(f"[!] Failed to send payload: {e}")

if __name__ == "__main__":
    send_payload()
