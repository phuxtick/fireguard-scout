# fireguard_scout/metrics.py

import psutil

def get_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return {
        "cpu_percent": round(cpu_percent, 1),
        "mem_percent": round(mem.percent, 1),
        "disk_percent": round(disk.percent, 1)
    }
