import tkinter as tk

WHITE = "#FFF"
LIGHT_GREY = "#D3D3D3"
LABEL_COLOR = "#25265E"
SMALL_FONT_STYLE = ("arial", 16)
BIG_FONT_STYLE = ('arial', 41, "bold")
DIGITS_POLICE = ("arial", 24, "bold")
DEFAULT_POLICE = ("arial", 20)
OFF_WHITE = "#FAFAFF"
LIGHT_BLUE="#CCDDFF"

class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculatrice")
        self.current_expression = "0"
        self.total_expression = "0"
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        # \u00F7 et l'autre ce sont deux valeur unicode qui representes ls deux symboles de devision et de multiplication
        self.buttons_frame = self.create_button_frame()
        self.create_digits_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_special_buttons(self):
        self.create_create_clear_button()
        self.create_create_equals_button()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GREY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digits_buttons(self):
        for digits, grid in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digits), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_POLICE,
                               borderwidth=0)
            button.grid(row=grid[0], column=grid[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, font=DEFAULT_POLICE, bg=OFF_WHITE, fg=LABEL_COLOR,
                               borderwidth=0)
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i = i +1

    def create_create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", font=DEFAULT_POLICE, bg=OFF_WHITE, fg=LABEL_COLOR,
                           borderwidth=0)
        button.grid(row=0, column=1, columnspan=3,sticky=tk.NSEW)

    def create_create_equals_button(self):
        button = tk.Button(self.buttons_frame, text='=', font=DEFAULT_POLICE, bg=LIGHT_BLUE, fg=LABEL_COLOR,
                           borderwidth=0)
        button.grid(row=4, column=3, columnspan=2,sticky=tk.NSEW)

    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, fg=LABEL_COLOR,
                               bg=LIGHT_GREY, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, fg=LABEL_COLOR,
                         bg=LIGHT_GREY, padx=24, font=BIG_FONT_STYLE)
        label.pack(expand=True, fill="both")
        return total_label, label

    def run(self):
        self.window.mainloop()


obj = Calculator()
obj.run()
