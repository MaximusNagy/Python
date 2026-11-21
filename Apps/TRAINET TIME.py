import tkinter as tk
import time
import random
import threading
import winsound

class HIITTimerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HIIT Timer")
        self.geometry("500x400")
        self.resizable(False, False)
        
        # Default settings for HIIT intervals
        self.workout_time = 20  # seconds for workout
        self.rest_time = 10     # seconds for rest
        self.running = False
        self.paused = False
        self.skip = False  # flag to skip the current interval
        
        # List of HIIT exercises
        self.exercises = [
            "Burpees", 
            "High Knees", 
            "Mountain Climbers", 
            "Jumping Jacks", 
            "Squat Jumps", 
            "Plank Jacks"
        ]
        
        self.create_widgets()
        
    def create_widgets(self):
        # Frame for settings (enter workout and rest durations)
        settings_frame = tk.Frame(self)
        settings_frame.pack(pady=10)
        
        tk.Label(settings_frame, text="Workout Duration (seconds):", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
        self.workout_entry = tk.Entry(settings_frame, width=5, font=("Arial", 12))
        self.workout_entry.insert(0, str(self.workout_time))
        self.workout_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(settings_frame, text="Rest Duration (seconds):", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
        self.rest_entry = tk.Entry(settings_frame, width=5, font=("Arial", 12))
        self.rest_entry.insert(0, str(self.rest_time))
        self.rest_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Frame for control buttons
        control_frame = tk.Frame(self)
        control_frame.pack(pady=10)
        
        self.start_button = tk.Button(control_frame, text="Start HIIT", font=("Arial", 12), bg="green", fg="white", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=10)
        
        self.stop_button = tk.Button(control_frame, text="Stop", font=("Arial", 12), bg="red", fg="white", command=self.stop_timer)
        self.stop_button.grid(row=0, column=1, padx=10)
        
        self.pause_button = tk.Button(control_frame, text="Pause", font=("Arial", 12), bg="yellow", fg="black", command=self.pause_timer)
        self.pause_button.grid(row=0, column=2, padx=10)
        
        self.resume_button = tk.Button(control_frame, text="Resume", font=("Arial", 12), bg="blue", fg="white", command=self.resume_timer)
        self.resume_button.grid(row=0, column=3, padx=10)
        
        self.skip_button = tk.Button(control_frame, text="Skip", font=("Arial", 12), bg="purple", fg="white", command=self.skip_timer)
        self.skip_button.grid(row=0, column=4, padx=10)
        
        # Frame for display: current exercise and countdown timer
        display_frame = tk.Frame(self)
        display_frame.pack(pady=20)
        
        self.exercise_label = tk.Label(display_frame, text="Press 'Start HIIT' to begin", font=("Arial", 16), fg="blue")
        self.exercise_label.pack(pady=10)
        
        self.timer_label = tk.Label(display_frame, text="00:00", font=("Arial", 36), fg="red")
        self.timer_label.pack(pady=10)
        
        # Status message label
        self.status_label = tk.Label(self, text="", font=("Arial", 12), fg="green")
        self.status_label.pack(pady=10)
        
    def play_sound(self):
        # Produce a beep sound using winsound (Windows only)
        winsound.Beep(1000, 500)  # frequency 1000 Hz, duration 500 ms
        
    def update_timer(self, label_text, duration):
        remaining = duration
        while remaining > 0 and self.running:
            # Pause handling: wait if paused
            while self.paused and self.running:
                self.status_label.config(text="Paused", fg="orange")
                self.update()
                time.sleep(0.1)
            # If skip flag is set, break the current interval loop
            if self.skip:
                break
            mins, secs = divmod(remaining, 60)
            self.timer_label.config(text=f"{mins:02}:{secs:02}")
            self.status_label.config(text=label_text, fg="green")
            self.update()
            time.sleep(1)
            remaining -= 1
        # Reset skip flag after the interval
        self.skip = False
            
    def hiit_cycle(self):
        try:
            self.workout_time = int(self.workout_entry.get())
            self.rest_time = int(self.rest_entry.get())
        except ValueError:
            self.status_label.config(text="Please enter valid numbers for time.", fg="red")
            self.running = False
            return
        
        # Shuffle the list of exercises
        random.shuffle(self.exercises)
        
        while self.running:
            for exercise in self.exercises:
                if not self.running:
                    break
                # Begin workout interval for the current exercise
                self.play_sound()
                self.exercise_label.config(text=f"Exercise: {exercise}")
                self.update_timer("Workout", self.workout_time)
                if not self.running:
                    break
                # Begin rest interval
                self.play_sound()
                self.exercise_label.config(text="Rest")
                self.update_timer("Rest", self.rest_time)
            # Reshuffle for the next round of exercises
            random.shuffle(self.exercises)
    
    def start_timer(self):
        if self.running:
            return
        self.running = True
        self.paused = False
        self.status_label.config(text="HIIT in progress...", fg="green")
        self.thread = threading.Thread(target=self.hiit_cycle, daemon=True)
        self.thread.start()
    
    def stop_timer(self):
        self.running = False
        self.paused = False
        self.status_label.config(text="Stopped", fg="red")
    
    def pause_timer(self):
        if self.running:
            self.paused = True
            self.status_label.config(text="Paused", fg="orange")
    
    def resume_timer(self):
        if self.running and self.paused:
            self.paused = False
            self.status_label.config(text="HIIT in progress...", fg="green")
            
    def skip_timer(self):
        if self.running:
            self.skip = True
            self.status_label.config(text="Skipping current interval...", fg="purple")
    
if __name__ == "__main__":
    app = HIITTimerApp()
    app.mainloop()
