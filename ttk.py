import requests as req
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class SearchBar(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(padx=20, pady=(0, 20), fill=BOTH, expand=True)
        self.label_text = ttk.StringVar(value="No QUERY")

        self.search_bar = ttk.Entry(self, font=("Garamond", 12))
        self.search_button = ttk.Button(self, text="Search", command=self.get_records)
        self.results_label = ttk.Label(self, textvariable=self.label_text, font=("Garamond", 12), justify=CENTER)    

        self.results_label.pack(expand=True, padx=20, pady=20, side=BOTTOM)
        self.search_bar.pack(side=LEFT, fill=X, expand=True)
        self.search_button.pack(side=LEFT, padx=(5, 0))


    def get_records(self):
        name = self.search_bar.get()
        if len(name) < 1:
            self.label_text.set(value="IMPROPER QUERY")
        else:
            url_string = f"https://192.168.1.29:8000/names/{name}"
            response = req.get(url_string).json()
            if "msg" in response:
                self.label_text.set(value=response["msg"])
            else:
                response_string = f"""
                Name: {response["name"]}
                Age: {response["age"]}
                Favorite Game: {response["favgame"]}
                """
                self.label_text.set(value=response_string)


class ButtonGroup(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=20, pady=20, fill=X)

        self.submit_button = ttk.Button(self, text="Submit", bootstyle=SUCCESS)
        self.cancel_button = ttk.Button(self, text="Cancel", bootstyle=(OUTLINE, SECONDARY))

        self.submit_button.pack(side=RIGHT, padx=(20, 0))
        self.cancel_button.pack(side=RIGHT)


class GameSearchWindow(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.label_title = ttk.Label(self, text="SMIC GAMING RECORDS", bootstyle=PRIMARY, font=("Garamond", 39, "bold"))
        self.label_two = ttk.Label(self, text="A great tool for finding random SMIC students and their favorite games", bootstyle=SECONDARY, font=("Garamond", 20))

        self.label_title.pack(padx=20, pady=(20, 10), anchor=W)
        self.label_two.pack(padx=20, pady=(0, 20), anchor=W)
        self.search_bar = SearchBar(self)


class FoodSearchWindow(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.label_title = ttk.Label(self, text="FOOD RECORDS", bootstyle=PRIMARY, font=("Garamond", 39, "bold"))
        self.label_two = ttk.Label(self, text="A great tool for finding random food items and some cool facts/details", bootstyle=SECONDARY, font=("Garamond", 20))

        self.label_title.pack(padx=20, pady=(20, 10), anchor=W)
        self.label_two.pack(padx=20, pady=(0, 20), anchor=W)
        self.search_bar = SearchBar(self)


class App(ttk.Window):

    def __init__(self, theme):
        super().__init__(themename=theme)

        self.title("SMIC RECORDS")
        self.geometry("1280x720")

        self.nav_frame = ttk.Frame(self, bootstyle=PRIMARY)
        self.nav_frame.pack(fill=X, ipadx=5, ipady=5)

        self.container = ttk.Frame(self)
        self.container.pack(fill=BOTH, expand=True)

        self.game_button = ttk.Button(self.nav_frame, text="Gaming Records", bootstyle=SECONDARY, command=lambda: self.change_frame("gaming"))
        self.food_button = ttk.Button(self.nav_frame, text="Food Records", bootstyle=SECONDARY, command=lambda: self.change_frame("food"))

        self.food_button.pack(side=RIGHT, padx=5)
        self.game_button.pack(side=RIGHT, padx=5)

        self.frames = {
            "gaming": GameSearchWindow(self.container),
            "food": FoodSearchWindow(self.container)
        }
        
        self.current_frame = "gaming"

    def set_frame(self):
        self.frames[self.current_frame].pack(fill=BOTH, expand=True)

    def remove_frame(self):
        self.frames[self.current_frame].pack_forget()

    def change_frame(self, name):
        self.remove_frame()
        self.current_frame = name
        self.set_frame()


if __name__ == "__main__":
    app = App(theme="vapor")
    app.place_window_center()
    app.mainloop()