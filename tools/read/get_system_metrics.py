import os
import psutil
import json

def get_system_metrics() -> str:
    print("DEBUG: Entering get_system_metrics()")
    """Returns CPU Usage, RAM Usage and C:/ Drive space"""
    """Args:None, Return {CPU USAGE (percent), RAM USAGE (percent), DISK FREE (GB), DISK TOTAL (GB)}"""
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")

    """Converting Disk Metrics to GB"""
    disk_free_gb = round(disk.free / (1024**3),ndigits=2)
    disk_total_gb = round(disk.total / (1024**3),ndigits=2)

    results = json.dumps({
        "CPU USAGE (Percent)": cpu,
        "RAM USAGE (Percent)": ram.percent,
        "DISK FREE (GB)": disk_free_gb,
        "DISK TOTAL (GB)": disk_total_gb
    },indent=4)

    return results

if __name__ == "__main__":
    print(get_system_metrics())