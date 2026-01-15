import os # For interacting with the operating system
import platform # For retrieving system information
import socket # For getting the hostname

def get_pc_info():
    """Retrieve and return basic PC information."""
    pc_info = {
        "Hostname": socket.gethostname(),
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Machine Type": platform.machine(),
        "Processor": platform.processor()
    }
    return pc_info

def display_pc_info():
    """Display the PC information."""
    pc_info = get_pc_info()
    print("PC Information:")
    for key, value in pc_info.items():
        print(f"{key}: {value}")
        
if __name__ == "__main__":  
    display_pc_info()