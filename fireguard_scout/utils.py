import socket
import psutil
import platform

def get_ip_addresses():
    ip_map = {}
    for iface_name, iface_addrs in psutil.net_if_addrs().items():
        for addr in iface_addrs:
            if addr.family == socket.AF_INET and not addr.address.startswith("127."):
                ip_map[iface_name] = addr.address
    return ip_map

def get_os_info():
    os_version = "unknown"
    try:
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("VERSION_ID="):
                    os_version = line.strip().split("=")[1].strip('"')
                    break
    except FileNotFoundError:
        pass

    kernel_version = platform.release()
    return {
        "os_version": os_version,
        "kernel_version": kernel_version
    }