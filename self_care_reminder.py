import tkinter as tk
from tkinter import messagebox
import threading
import time

class SelfCareReminderApp:
    def __init__(self, root):
        import random
        self.random = random
        self.messages = [
            "Time for a break! ✨\nStretch your body and breathe deeply. 😊",
            "Hydrate yourself! 💧 Grab some water.",
            "Rest your eyes for a minute. 👀",
            "Stand up and walk around! 🚶‍♂️",
            "Walk outside and breathe in the fresh air. 🧘‍♂️",
            "Smile and relax your shoulders! 😄",
            "Take some vitamins. 🍊",
            "Look outside and enjoy the view. 🌳",
            "Do a quick stretch! 🤸‍♀️",
            "Eat a snack. 😋",
            "Write down something you're grateful for. 📝",
            "Listen to your favorite song for a moment. 🎵"
        ]
        self.root = root
        self.root.title("🍃😮‍💨 Care4U 🍁😌")
        self.root.geometry("370x230")
        self.root.configure(bg="#e18e3b")  # Autumn cream background

        self.interval_var = tk.IntVar(value=60)
        self.running = False
        self.thread = None

        title_label = tk.Label(root, text="Take Care of Yourself! 🍁🍂🎃", font=("Helvetica", 16, "bold"), fg="#8B4513", bg="#e18e3b")
        title_label.pack(pady=8)

        self.emoji_label = tk.Label(root, text="🍁🍂🎃🌰🧣", font=("Helvetica", 18), bg="#e18e3b")
        interval_label = tk.Label(root, text="Set reminder interval (minutes):", font=("Helvetica", 12), fg="#8B4513", bg="#e18e3b")  # Autumn orange background
        interval_label.pack(pady=6)
        tk.Entry(root, textvariable=self.interval_var, width=10, font=("Helvetica", 12), bg="#FFF8DC", fg="#FF9800").pack()

        self.start_btn = tk.Button(root, text="Start Reminders 🍂", command=self.start_reminders, font=("Helvetica", 12), bg="#FFA07A", fg="#8B4513", activebackground="#FFD700")
        self.start_btn.pack(pady=10)
        self.stop_btn = tk.Button(root, text="Stop Reminders 🛑", command=self.stop_reminders, state=tk.DISABLED, font=("Helvetica", 12), bg="#DEB887", fg="#8B0000", activebackground="#FFDAB9")
        self.stop_btn.pack()

        self.emoji_label = tk.Label(root, text="🍁🍂🎃🌰🧣", font=("Helvetica", 18), bg="#e18e3b")
        self.emoji_label.pack(pady=8)

    def start_reminders(self):
        if not self.running:
            self.running = True
            self.start_btn.config(state=tk.DISABLED)
            self.stop_btn.config(state=tk.NORMAL)
            self.thread = threading.Thread(target=self.reminder_loop, daemon=True)
            self.thread.start()

    def stop_reminders(self):
        self.running = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)

    def reminder_loop(self):
        interval = self.interval_var.get() * 60
        while self.running:
            time.sleep(interval)
            if self.running:
                self.show_reminder()

    def show_reminder(self):
        # Animate emoji label (simple color flash)
        self.flash_emoji()
        msg = self.random.choice(self.messages)
        autumn_emojis = ["🍁", "🍂", "🎃", "🌰", "🧣", "🦉", "🍎", "🍃"]
        autumn_msg = f"{self.random.choice(autumn_emojis)} {msg} {self.random.choice(autumn_emojis)}"
        messagebox.showinfo("🍁 Autumn Self-Care Reminder �", autumn_msg)

    def flash_emoji(self):
        # Combination animation: color flash, emoji swap, and font size bounce
        original_bg = self.emoji_label.cget("bg")
        original_text = self.emoji_label.cget("text")
        original_font = self.emoji_label.cget("font")
        emojis = ["✨😊🌻🧘‍♂️💧", "💪😃🌸🧘‍♀️🍵", "🌞😌🌿🦋💦", "🧘‍♂️🍀😄🎧🥤", "🌻🧘‍♀️💧😊✨"]

        def step1():
            self.emoji_label.config(bg="#ffffe0", text=self.random.choice(emojis), font=("Helvetica", 22))
            self.root.after(200, step2)

        def step2():
            self.emoji_label.config(bg="#e18e3b", font=("Helvetica", 26))
            self.root.after(200, step3)

        def step3():
            self.emoji_label.config(bg=original_bg, text=original_text, font=original_font)

        step1()

if __name__ == "__main__":
    root = tk.Tk()
    app = SelfCareReminderApp(root)
    root.mainloop()
