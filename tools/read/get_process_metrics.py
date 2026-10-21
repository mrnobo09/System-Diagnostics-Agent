import psutil
import json

def get_process_metrics(sort_by : str = 'cpu_percent', top_N:int = 10) -> str:
    print(f"DEBUG: Entering get_process_metrics(sort_by={sort_by}, top_N={top_N})")
    """List System Processes and sort them by Usage CPU (Default) or RAM and returns Top N (default = 10) results"""
    processes = []
    attrs = ['pid','name','status','memory_percent','cpu_percent']


    for proc in psutil.process_iter(['cpu_percent']):
            try:
                proc.info['cpu_percent']
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass


    for process in psutil.process_iter(attrs):
        try:
            if process.info['pid'] == 0:
                continue
            
            if process.info['memory_percent'] or process.info['cpu_percent'] is not None:
                process.info['memory_percent'] = round(process.info['memory_percent'],2)
                process.info['cpu_percent'] = round(process.info['cpu_percent'],2) / psutil.cpu_count()

            processes.append(process.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Ignore processes that close during execution or lack permissions
            pass

    sorted_processes = sorted(
         processes,
         key = lambda x: x.get(sort_by,0.0),
         reverse=True
    )

    return json.dumps(sorted_processes[:top_N],indent=4)

    

if __name__ == "__main__":
    print(get_process_metrics())
    