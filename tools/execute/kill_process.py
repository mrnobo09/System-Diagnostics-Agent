import psutil

def kill_process(pid:int) -> bool:
    print(f"DEBUG: Entering kill_process(pid={pid})")
    """Kills process via pid"""
    """Args (pid:int), Return (bool)"""
    
    try:
        psutil.Process(pid).kill()
        return True
    except psutil.NoSuchProcess:
        return False
    except psutil.AccessDenied:
        # return f"Error: Permission denied. Run your script with elevated/admin rights to kill PID {pid}."
        return False
    except psutil.TimeoutExpired:
        # return f"Warning: Sent kill signal to PID {pid}, but it didn't exit within 3 seconds."
        return False