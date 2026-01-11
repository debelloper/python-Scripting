import os
import platform
import sys


# Function to shut down the PC
def shutdown_pc(): 
    sys_platform = platform.system()
    
    if platform.system() == "Linux" or platform.system() == "Darwin":  # macOS is identified as 'Darwin'
        os.system("sudo shutdown -h now")
    else: # Assuming Windows
        os.system("shutdown /s /t 0")

if __name__ == "__main__":
    shutdown_pc()