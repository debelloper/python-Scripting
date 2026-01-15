import os # For interacting with the operating system
import sys # For accessing command-line arguments
import subprocess # For executing system commands
import argparse # For parsing command-line arguments

def toggle_antivirus(action): # Function to turn antivirus on or off
    """Toggle the antivirus state based on the action provided."""
    if os.name == 'nt':  # Windows
        if action == 'on':
            subprocess.run(['powershell', '-Command', 'Set-MpPreference -DisableRealtimeMonitoring $false'])
            print("Antivirus turned ON.")
        elif action == 'off':
            subprocess.run(['powershell', '-Command', 'Set-MpPreference -DisableRealtimeMonitoring $true'])
            print("Antivirus turned OFF.")
        else:
            print("Invalid action. Use 'on' or 'off'.")
    else:
        print("This script is only supported on Windows.") # Notify user if not on Windows

# for linux
def toggle_antivirus_linux(action):
    """Toggle the antivirus state based on the action provided for Linux."""
    if action == 'on':
        subprocess.run(['sudo', 'systemctl', 'start', 'clamav-daemon'])
        print("Antivirus turned ON.")
    elif action == 'off':
        subprocess.run(['sudo', 'systemctl', 'stop', 'clamav-daemon'])
        print("Antivirus turned OFF.")
    else:
        print("Invalid action. Use 'on' or 'off'.")

def main():
    parser = argparse.ArgumentParser(description="Turn antivirus on or off.")
    parser.add_argument("action", choices=['on', 'off'], help="Action to perform: 'on' to enable antivirus, 'off' to disable antivirus")
    
    args = parser.parse_args()
    
    toggle_antivirus(args.action)

if __name__ == "__main__": # Entry point of the script
    main()