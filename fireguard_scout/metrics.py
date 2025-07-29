# fireguard_scout/utils.py
import psutil
import socket

def get_ip_addresses():
    ip_map = {}

    for iface_name, iface_addrs in psutil.net_if_addrs().items():
        for addr in iface_addrs:
            if addr.family == socket.AF_INET and not addr.address.startswith("127."):
                ip_map[iface_name] = addr.address

    return ip_map
