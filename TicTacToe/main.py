import tkinter as tk
from tkinter import font

class TTTboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Zeros & Incorrects")
        self._cells = {}

        def make_board_display(self):
            display_frame = tk.Frame(master=self)
            display_frame.pack(fill=tk.X)
            self.display = tk.Label(
                master=display_frame,
                text="Ready",
                font=font.font(size=30, weight="bold"),
            )
            self.display.pack()


