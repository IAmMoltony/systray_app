#!/usr/bin/env python3

import tkinter as tk
import pystray
from PIL import Image

class SystrayApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Systray App")
        self.geometry("640x480")
        self.protocol("WM_DELETE_WINDOW", self.min_to_tray)

        tk.Label(self, text = "This is a systray app").place(x = 15, y = 15)

        print("Systray App initialized")

    def min_to_tray(self):
        print("Minimizing to tray")

        self.withdraw()
        image = Image.open("app.ico")
        menu = (pystray.MenuItem("Quit", self.quit_window),
                pystray.MenuItem("Show", self.show_window))
        icon = pystray.Icon("name", image, "Systray App", menu)
        icon.run()

    def quit_window(self, icon):
        print("Quitting app")

        icon.stop()
        self.destroy()

    def show_window(self, icon):
        print("Showing window")

        icon.stop()
        self.after(0, self.deiconify)

if __name__ == "__main__":
    SystrayApp().mainloop()
