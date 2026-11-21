import tkinter as tk
from tkinter import messagebox
import requests
import threading
import time
from plyer import notification

# Replace with your actual OpenWeatherMap API key
API_KEY = 'your_api_key_here'

def get_weather(city):
    """Fetches weather info for a city and returns a formatted string."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"].capitalize()
            return f"{city}: {temp}°C, {description}"
        else:
            return f"Weather data not found for '{city}'."
    except Exception as e:
        return f"Error: {e}"

def send_notification(message):
    """Sends a desktop notification with the given message."""
    notification.notify(
        title="Live Weather Update",
        message=message,
        timeout=10  # Notification duration in seconds
    )

def update_weather():
    """Retrieves city input, updates the GUI, and sends a notification."""
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return
    weather = get_weather(city)
    result_label.config(text=weather)
    send_notification(weather)

def start_auto_update(interval=3600):
    """Automatically updates weather every 'interval' seconds."""
    while True:
        update_weather()
        time.sleep(interval)

def schedule_updates():
    """Starts periodic weather updates in a background thread."""
    thread = threading.Thread(target=start_auto_update, daemon=True)
    thread.start()

# ------------------- Tkinter GUI Setup -------------------
root = tk.Tk()
root.title("Live Weather Notifications - Egypt Example")
root.geometry("400x250")
root.resizable(False, False)

# Instruction label
tk.Label(root, text="Enter City (e.g., Cairo):", font=("Arial", 12)).pack(pady=10)

# Entry widget for city name (default set to 'Cairo' for Egypt)
city_entry = tk.Entry(root, font=("Arial", 12), width=30)
city_entry.pack()
city_entry.insert(0, "Cairo")

# Button to fetch weather immediately
tk.Button(root, text="Get Weather Now", font=("Arial", 12), command=update_weather).pack(pady=10)

# Button to start periodic (hourly) weather updates
tk.Button(root, text="Start Auto Update (Hourly)", font=("Arial", 10), command=schedule_updates).pack(pady=5)

# Label to display weather result in the GUI
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=380)
result_label.pack(pady=10)

root.mainloop()
