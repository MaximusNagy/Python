import subprocess

def get_saved_wifi_passwords():
    # Get a list of saved WiFi profiles
    result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
    profiles = [line.split(":")[1].strip() for line in result.stdout.split("\n") if "All User Profile" in line]

    wifi_data = {}
    
    for profile in profiles:
        # Get WiFi password for each saved network
        result = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True)
        lines = result.stdout.split("\n")
        for line in lines:
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                wifi_data[profile] = password
                break
        else:
            wifi_data[profile] = "No password found"

    return wifi_data

# Print saved WiFi passwords
wifi_passwords = get_saved_wifi_passwords()
for wifi, password in wifi_passwords.items():
    print(f"WiFi: {wifi} | Password: {password}")
