import psutil
import socket
import json
from datetime import datetime, timezone

def collect_metrics():
    net = psutil.net_io_counters()

    metrics = {
        "server_id": socket.gethostname(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
        "network_sent_mb": round(net.bytes_sent / (1024 * 1024), 2),
        "network_recv_mb": round(net.bytes_recv / (1024 * 1024), 2),
    }
    return metrics

if __name__ == "__main__":
    data = collect_metrics()
    print(json.dumps(data, indent=2))