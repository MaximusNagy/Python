import platform
import subprocess
import os

def change_dns_windows(interface, primary_dns, secondary_dns):
    """
    Change DNS settings on Windows using netsh command.
    """
    try:
        # Set primary DNS
        command1 = f'netsh interface ip set dns name="{interface}" static {primary_dns} primary'
        # Add secondary DNS
        command2 = f'netsh interface ip add dns name="{interface}" {secondary_dns} index=2'
        
        print("Changing DNS settings on Windows...")
        subprocess.run(command1, shell=True, check=True)
        subprocess.run(command2, shell=True, check=True)
        print("DNS settings changed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error occurred while changing DNS settings:", e)

def change_dns_linux(primary_dns, secondary_dns):
    """
    Change DNS settings on Linux by modifying /etc/resolv.conf.
    """
    try:
        print("Changing DNS settings on Linux...")
        resolv_conf = "/etc/resolv.conf"
        with open(resolv_conf, "w") as f:
            f.write(f"nameserver {primary_dns}\n")
            f.write(f"nameserver {secondary_dns}\n")
        print("DNS settings changed successfully.")
        print("Note: Some services (like Network Manager) may override these changes.")
    except Exception as e:
        print("Error occurred while changing DNS settings:", e)

def main():
    # Example DNS servers (Google Public DNS)
    primary_dns = "8.8.8.8"
    secondary_dns = "8.8.4.4"
    
    system_os = platform.system()
    print("Detected OS:", system_os)
    
    if system_os == "Windows":
        interface = input("Enter network interface name (e.g., Wi-Fi, Ethernet): ")
        change_dns_windows(interface, primary_dns, secondary_dns)
    elif system_os == "Linux":
        if os.geteuid() != 0:
            print("Please run this script as root (sudo) to change DNS settings on Linux.")
            return
        change_dns_linux(primary_dns, secondary_dns)
    else:
        print("Unsupported OS. This script currently supports Windows and Linux.")

if __name__ == "__main__":
    main()
