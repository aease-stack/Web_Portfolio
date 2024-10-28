import tkinter as tk
import pyautogui
import threading
import time
import random

class AutoClicker:
    def __init__(self):
        self.running = False
        self.min_click_interval = 0
        self.max_click_interval = 0 

    def start_clicking(self):
        self.running = True
        while self.running:
            pyautogui.click()
            # Generate a random interval within the defined range
            interval = random.uniform(self.min_click_interval, self.max_click_interval) / 1000.0  # Convert to seconds
            
            # Debugging output to verify interval
            print(f"Interval: {interval} seconds (Min: {self.min_click_interval} Max: {self.max_click_interval})")
            
            time.sleep(interval)

    def stop_clicking(self):
        self.running = False

class App:
    def __init__(self, master):
        self.master = master
        master.title("Auto Clicker")

        self.autoclicker = AutoClicker()

        self.start_button = tk.Button(master, text="Start", command=self.start_clicking)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_clicking)
        self.stop_button.pack(pady=5)

        self.title_label = tk.Label(master, text="Click Interval Settings", font=("Arial", 14))
        self.title_label.pack(pady=10)

        self.min_click_interval_label = tk.Label(master, text="Min Click Interval (milliseconds):")
        self.min_click_interval_label.pack()
        self.min_click_interval_entry = tk.Entry(master)
        self.min_click_interval_entry.insert(0, "50")  
        self.min_click_interval_entry.pack(pady=5)

        self.max_click_interval_label = tk.Label(master, text="Max Click Interval (milliseconds):")
        self.max_click_interval_label.pack()
        self.max_click_interval_entry = tk.Entry(master)
        self.max_click_interval_entry.insert(0, "200") 
        self.max_click_interval_entry.pack(pady=5)

    def start_clicking(self):
        try:
            min_interval = int(self.min_click_interval_entry.get())
            max_interval = int(self.max_click_interval_entry.get())

            # Validate the input
            if min_interval < 0 or max_interval < 0:
                raise ValueError("Intervals must be non-negative.")
            if min_interval > max_interval:
                raise ValueError("Min Click Interval must be less than or equal to Max Click Interval.")

            # Set the click intervals
            self.autoclicker.min_click_interval = min_interval
            self.autoclicker.max_click_interval = max_interval

            # Start the clicking thread
            if not self.autoclicker.running:
                threading.Thread(target=self.autoclicker.start_clicking).start()
        except ValueError as e:
            print(f"Invalid input: {e}")

    def stop_clicking(self):
        self.autoclicker.stop_clicking()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
