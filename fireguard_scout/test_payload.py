from fireguard_scout.utils import get_ip_addresses, get_os_info
from datetime import datetime, timezone
import json

def main():
    hostname = "test-host"
    metrics = {
        "cpu_percent": 12.3,
        "mem_percent": 45.6,
        "disk_percent": 78.9
    }

    ip_data = get_ip_addresses()
    os_info = get_os_info()

    payload = {
        "hostname": hostname,
        "location": "unknown",
        "services": {
            "cpu": f"{metrics['cpu_percent']}%",
            "memory": f"{metrics['mem_percent']}%",
            "disk": f"{metrics['disk_percent']}%"
        },
        "interfaces": ip_data,
        "system_info": os_info,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    main()
