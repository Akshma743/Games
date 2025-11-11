import tkinter as tk
from tkinter import ttk
import threading
import time

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Process Control Example")
        self.root.geometry("300x180")

        # Label to display counter
        self.label = ttk.Label(root, text="Counter: 0", font=("Arial", 14))
        self.label.pack(pady=10)

        # Buttons
        self.start_button = ttk.Button(root, text="Start", command=self.start_counter)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop_counter)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.restart_button = ttk.Button(root, text="Restart", command=self.restart_counter)
        self.restart_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Variables
        self.running = False
        self.counter = 0

    def update_label(self):
        """Thread function to update the counter every second."""
        while self.running:
            time.sleep(1)
            self.counter += 1
            self.label.config(text=f"Counter: {self.counter}")

    def start_counter(self):
        """Start the counter if it's not already running."""
        if not self.running:
            self.running = True
            self.counter_thread = threading.Thread(target=self.update_label)
            self.counter_thread.daemon = True  # Allows program to exit cleanly
            self.counter_thread.start()

    def stop_counter(self):
        """Stop the counter."""
        self.running = False

    def restart_counter(self):
        """Restart the counter (reset to 0 and start again)."""
        self.stop_counter()
        self.counter = 0
        self.label.config(text="Counter: 0")
        self.start_counter()


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
