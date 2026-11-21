import win32gui
from pynput import mouse, keyboard
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
import time
import threading

# Global variables
events = []  # List to store recorded events
recording = False  # Recording status
target_title = "Roblox"  # Target window title (can be changed)

# Function to check if the target window is active
def is_target_window_active():
    active_window = win32gui.GetForegroundWindow()
    active_title = win32gui.GetWindowText(active_window)
    return target_title.lower() in active_title.lower()

# Record mouse movements
def on_move(x, y):
    if recording and is_target_window_active():
        timestamp = time.time()
        events.append(("move", x, y, timestamp))

def on_click(x, y, button, pressed):
    if recording and is_target_window_active() and pressed:
        timestamp = time.time()
        events.append(("click", x, y, str(button), timestamp))

# Record keyboard presses
def on_press(key):
    if recording and is_target_window_active():
        timestamp = time.time()
        try:
            events.append(("key_press", key.char, timestamp))
        except AttributeError:
            events.append(("key_press", str(key), timestamp))

# Function to start mouse and keyboard listeners
def start_listeners():
    mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click)
    keyboard_listener = keyboard.Listener(on_press=on_press)
    mouse_listener.start()
    keyboard_listener.start()
    return mouse_listener, keyboard_listener

# Function to replay events
def replay_events():
    if not events:
        print("No recorded events to replay!")
        return
    
    mouse_ctrl = MouseController()
    keyboard_ctrl = KeyboardController()
    start_time = events[0][3]  # Timestamp of the first event
    
    print("Starting replay...")
    for event in events:
        event_type, *args, timestamp = event
        delay = timestamp - start_time
        time.sleep(max(0, delay))  # Delay between events
        
        if not is_target_window_active():
            print("Replay stopped because the window is not active!")
            break
        
        if event_type == "move":
            x, y = args[0], args[1]
            mouse_ctrl.position = (x, y)
        elif event_type == "click":
            x, y, button = args[0], args[1], args[2]
            mouse_ctrl.position = (x, y)
            mouse_ctrl.click(mouse.Button.left if "left" in button else mouse.Button.right)
        elif event_type == "key_press":
            key = args[0]
            keyboard_ctrl.press(key)
            keyboard_ctrl.release(key)
    
    print("Replay finished.")

# Main interface
def main():
    global recording
    print(f"Macro system for '{target_title}'")
    print("Commands:")
    print("  1 - Start recording")
    print("  2 - Stop recording")
    print("  3 - Replay events")
    print("  4 - Exit")

    # Start mouse and keyboard listeners in a separate thread
    mouse_listener, keyboard_listener = start_listeners()

    while True:
        command = input("Enter command (1-4): ").strip()
        
        if command == "1":
            if not recording:
                if is_target_window_active():
                    events.clear()  # Clear previous events
                    recording = True
                    print("Starting recording...")
                else:
                    print(f"Please activate the '{target_title}' window first!")
            else:
                print("Recording is already in progress!")
        
        elif command == "2":
            if recording:
                recording = False
                print(f"Recording stopped. Number of recorded events: {len(events)}")
            else:
                print("No recording in progress!")
        
        elif command == "3":
            if not recording:
                replay_events()
            else:
                print("Please stop recording first!")
        
        elif command == "4":
            print("Exiting the program...")
            mouse_listener.stop()
            keyboard_listener.stop()
            break
        
        else:
            print("Invalid command! Please choose 1-4.")

if __name__ == "__main__":
    main()