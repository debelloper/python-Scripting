import os
import platform
import sys
import subprocess
import time


# close all apps before shutting down

# Requesting administrative privileges on Windows
if time.platform == "win32":
    import ctypes
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

# Function to shut down the PC
def shutdown_pc(): 

    sys_platform = platform.system()
    
    if platform.system() == "Linux" or platform.system() == "Darwin":  # macOS is identified as 'Darwin'
        subprocess.run(["sudo", "shutdown", "-h", "now"])
    else: # Assuming Windows
        os.system("shutdown /s /t 0")

if __name__ == "__main__":
    shutdown_pc()
# Note: This script requires administrative privileges to execute the shutdown command.