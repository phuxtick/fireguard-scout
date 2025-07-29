from fireguard_scout.utils import get_ip_addresses
from datetime import datetime, timezone
from fireguard_scout.utils import get_os_info


def main():
    hostname = "test-host"
    metrics = {
        "cpu_percent": 12.3,
        "mem_percent": 45.6,
        "disk_percent": 78.9
        
    }

    os_info = get_os_info()
    print("OS Info:", os_info)

    payload = {
        "hostname": hostname,
        "location": "unknown",
        "services": {
            "cpu": f"{metrics['cpu_percent']}%",
            "memory": f"{metrics['mem_percent']}%",
            "disk": f"{metrics['disk_percent']}%"
        },
        "interfaces": get_ip_addresses(),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    import json
    print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    main()
