import tkinter as tk
from tkinter import messagebox

class TimerApp:
    def __init__(self, root):
        self.root = root
        root.title("Timer App")

        # Variables
        self.hour_var = tk.IntVar()
        self.minute_var = tk.IntVar()
        self.second_var = tk.IntVar()

        self.timer_running = False
        self.remaining_seconds = 0

        # Layout
        tk.Label(root, text="Hour:").grid(row=0, column=0, padx=5, pady=5)
        self.hour_spin = tk.Spinbox(root, from_=0, to=23, width=5, textvariable=self.hour_var)
        self.hour_spin.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Minute:").grid(row=0, column=2, padx=5, pady=5)
        self.minute_spin = tk.Spinbox(root, from_=0, to=59, width=5, textvariable=self.minute_var)
        self.minute_spin.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(root, text="Second:").grid(row=0, column=4, padx=5, pady=5)
        self.second_spin = tk.Spinbox(root, from_=0, to=59, width=5, textvariable=self.second_var)
        self.second_spin.grid(row=0, column=5, padx=5, pady=5)

        self.set_button = tk.Button(root, text="Set", command=self.start_timer)
        self.set_button.grid(row=0, column=6, padx=5, pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, state='disabled')
        self.stop_button.grid(row=0, column=7, padx=5, pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer, state='disabled')
        self.reset_button.grid(row=0, column=8, padx=5, pady=5)

        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 32))
        self.time_label.grid(row=1, column=0, columnspan=9, pady=20)

    def start_timer(self):
        if not self.timer_running:
            hours = self.hour_var.get()
            minutes = self.minute_var.get()
            seconds = self.second_var.get()
            self.remaining_seconds = hours * 3600 + minutes * 60 + seconds
        if self.remaining_seconds <= 0:
            messagebox.showwarning("Warning", "Please set a time greater than 0.")
            return
        self.timer_running = True
        self.set_button.config(state='disabled')
        self.stop_button.config(state='normal')
        self.reset_button.config(state='normal')
        self.update_timer()

    def update_timer(self):
        if self.timer_running:
            h = self.remaining_seconds // 3600
            m = (self.remaining_seconds % 3600) // 60
            s = self.remaining_seconds % 60
            self.time_label.config(text=f"{h:02d}:{m:02d}:{s:02d}")
            if self.remaining_seconds == 0:
                self.timer_running = False
                self.set_button.config(state='normal')
                self.stop_button.config(state='disabled')
                self.reset_button.config(state='normal')
                messagebox.showinfo("Time's up", "Time's up!")
            else:
                self.remaining_seconds -= 1
                self.root.after(1000, self.update_timer)

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.set_button.config(state='normal')
            self.stop_button.config(state='disabled')
            self.reset_button.config(state='normal')

    def reset_timer(self):
        self.timer_running = False
        self.hour_var.set(0)
        self.minute_var.set(0)
        self.second_var.set(0)
        self.remaining_seconds = 0
        self.time_label.config(text="00:00:00")
        self.set_button.config(state='normal')
        self.stop_button.config(state='disabled')
        self.reset_button.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()