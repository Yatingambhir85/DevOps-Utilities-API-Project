import psutil

def get_system_metrics():
    """Fetches system metrics such as CPU and memory usage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    cpu_threshold = 80  # Example threshold for high CPU usage
    if cpu_usage > cpu_threshold:
        status = "High CPU Usage"
    else:
        status = "CPU Usage is Normal"
    return {
        "cpu_usage": cpu_usage,
        "memory_info": memory_info,
        "disk_usage": disk_usage,
        "status": status
    }