import pyautogui
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import time
import os

class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Автокликер")
        self.running = False
        self.image_path = None
        self.delay = 0.2

        self.build_gui()

    def build_gui(self):
        tk.Label(self.root, text="Задержка между кликами (сек):").pack(pady=5)
        self.delay_entry = tk.Entry(self.root)
        self.delay_entry.insert(0, "0.2")
        self.delay_entry.pack(pady=5)

        self.load_button = tk.Button(self.root, text="Выбрать изображение", command=self.choose_image)
        self.load_button.pack(pady=5)

        self.start_button = tk.Button(self.root, text="Старт", command=self.start_clicker, bg='green', fg='white')
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Стоп", command=self.stop_clicker, bg='red', fg='white')
        self.stop_button.pack(pady=5)

    def choose_image(self):
        path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if path:
            self.image_path = path
            messagebox.showinfo("Файл выбран", f"Файл: {os.path.basename(path)}")

    def start_clicker(self):
        if not self.image_path:
            messagebox.showerror("Ошибка", "Сначала выбери изображение!")
            return
        try:
            self.delay = float(self.delay_entry.get())
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат задержки.")
            return

        if not self.running:
            self.running = True
            threading.Thread(target=self.click_loop, daemon=True).start()

    def stop_clicker(self):
        self.running = False

    def click_loop(self):
        while self.running:
            location = pyautogui.locateCenterOnScreen(self.image_path, confidence=0.8)
            if location:
                pyautogui.click(location)
                print(f"Клик по: {location}")
            time.sleep(self.delay)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClickerApp(root)
    root.mainloop()
