import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class App(ttk.Window):

    def __init__(self, theme):
        super().__init__(themename=theme)


        self.button_one = ttk.Button(self, text="Submit", bootstyle=SUCCESS)
        self.button_two = ttk.Button(self, text="Cancel", bootstyle=(DANGER, OUTLINE))

        self.button_one.pack(padx=5, pady=10, side=LEFT)
        self.button_two.pack(padx=5, pady=10, side=RIGHT)


if __name__ == "__main__":
    app = App(theme="vapor")
    app.place_window_center()
    app.mainloop()