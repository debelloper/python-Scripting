import subprocess
import re

def scan_wifi():
    # Scan available WiFi networks
    result = subprocess.check_output("netsh wlan show networks", shell=True).decode()

    networks = []
    ssid = None

    for line in result.split("\n"):
        line = line.strip()

        if "SSID" in line and "BSSID" not in line:
            ssid = line.split(":")[1].strip()

        if "Authentication" in line:
            auth = line.split(":")[1].strip()

            # Check if network is open
            if auth.lower() == "open":
                networks.append(ssid)

    return networks


def connect_wifi(ssid):
    print(f"Connecting to open WiFi: {ssid}")
    subprocess.call(f'netsh wlan connect name="{ssid}"', shell=True)


def main():
    networks = scan_wifi()

    if not networks:
        print("No open WiFi networks found.")
        return

    # Connect to the first open network found
    connect_wifi(networks[0])


if __name__ == "__main__":
    main()