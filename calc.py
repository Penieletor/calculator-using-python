from tkinter import *

# Colors
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
WHITE = "#FFFFFF"
# fonts
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYEL = ("Arial", 40)
DIGITS_FONT_STYLE = ("Arial", 24, 'bold')
DEFAULT_FONT_STYLE = ("Arial", 20)
OFF_WHITE = "#F8F8FF"
LIGHT_BLUE = "#CCEDFF"


class Calculator:
    def __init__(self):
        self.window = Tk()
        self.TITLE = "Calculator"
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title(self.TITLE)

        self.total_display = ""
        self.current_display = ""

        # creating Frames

        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()

        # expanding the buttons to fill the button frame
        for x in range(1, 5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)
        # displays labels
        self.total_label, self.labels = self.create_display_label()

        self.create_digits_buttons()
        self.operator_buttons()

    def create_display_frame(self):
        frame = Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_button_frame(self):
        frame = Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    # updating the display labels

    def create_display_label(self):
        # labels to display the current and total expressions
        total_label = Label(self.display_frame,text=self.total_display, anchor=E, bg=LIGHT_GRAY, fg=LABEL_COLOR,
                            padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        label = Label(self.display_frame, text=self.current_display, anchor=E, bg=LIGHT_GRAY, fg=LABEL_COLOR,
                            padx=24, font=LARGE_FONT_STYEL)
        label.pack(expand=True, fill="both")

        return label, total_label

    # Functions
    def update_total_label(self):
        self.labels.config(text=self.total_display)

    def update_label(self):
        self.total_label.config(text=self.current_display[:11])
    # a function to display digits
    def add_expression(self, value):
        self.current_display += str(value)
        self.update_label()

    # function for clear operation
    def clear(self):
        self.current_display = ""
        self.total_display = ""
        self.update_total_label()
        self.update_label()

    # adding the operator to the display
    def append_operator(self, operator):
        self.current_display += operator
        self.total_display += self.current_display
        self.current_display = ""
        self.update_total_label()
        self.update_label()

    # function to add, multipy, divide etc
    def evaluate_solution(self):
        self.total_display += self.current_display
        self.update_total_label()
        try:
            self.current_display = str(eval(self.total_display))
            self.total_display = ""
        except Exception as p:
            self.current_display = "Error"
        finally:
            self.update_label()
    # function to square the number
    def square(self):
        self.current_display = str(eval(f"{self.current_display}**2"))
        self.update_label()

    def square_root(self):
        self.current_display = str(eval(f"{self.current_display}**0.5"))

    #creating numeric buttons
    def create_digits_buttons(self):
        buttons1 = Button(self.button_frame, text="1", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0,
                command=lambda: self.add_expression(1))
        buttons1.grid(row=3, column=3,  sticky=NSEW)
        buttons2 = Button(self.button_frame, text="2", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0,
                          command=lambda: self.add_expression(2))
        buttons2.grid(row=3, column=2,  sticky=NSEW)
        buttons3 = Button(self.button_frame, text="3", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0,
                          command=lambda: self.add_expression(3))
        buttons3.grid(row=3, column=1,  sticky=NSEW)
        buttons4 = Button(self.button_frame, text="4", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0,
                          command=lambda: self.add_expression(4))
        buttons4.grid(row=2, column=3,  sticky=NSEW)
        buttons5 = Button(self.button_frame, text="5", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0
                          ,command=lambda: self.add_expression(5))
        buttons5.grid(row=2, column=2,  sticky=NSEW)
        buttons6 = Button(self.button_frame, text="6", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0,
                          command=lambda: self.add_expression(6))
        buttons6.grid(row=2, column=1, sticky=NSEW)
        buttons7 = Button(self.button_frame, text="7", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0,
                          command=lambda: self.add_expression(7))
        buttons7.grid(row=1, column=1, sticky=NSEW)
        buttons8 = Button(self.button_frame, text="8", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0,
                          command=lambda: self.add_expression(8))
        buttons8.grid(row=1, column=2,  sticky=NSEW)
        buttons9 = Button(self.button_frame, text="9", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0,
                          command=lambda: self.add_expression(9))
        buttons9.grid(row=1, column=3, sticky=NSEW)
        buttons0 = Button(self.button_frame, text="0", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0,
                          command=lambda: self.add_expression(0))
        buttons0.grid(row=4,column=2,  sticky=NSEW)
        buttons_dot = Button(self.button_frame, text=".", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0,
                            command=lambda: self.add_expression("."))
        buttons_dot.grid(row=4,column=1,  sticky=NSEW)

    def operator_buttons(self):
        # row 1, row 2, row 3, row 4 and column 4
        add_operator = Button(self.button_frame, text="+", bg=OFF_WHITE, font=DEFAULT_FONT_STYLE, fg=LABEL_COLOR,
                              command=lambda :self.append_operator("+"))
        add_operator.grid(row=0, column=4, sticky=NSEW)
        mult_operator = Button(self.button_frame, text="*",bg=OFF_WHITE, font=DEFAULT_FONT_STYLE, fg=LABEL_COLOR,
                        command=lambda: self.append_operator("*"))
        mult_operator.grid(row=1, column=4, sticky=NSEW)

        divide_operator = Button(self.button_frame, text="/", bg=OFF_WHITE, font=DEFAULT_FONT_STYLE, fg=LABEL_COLOR,
                                 command=lambda: self.append_operator("/"))
        divide_operator.grid(row=2, column=4, sticky=NSEW)
        sub_operator = Button(self.button_frame, text="-", bg=OFF_WHITE, font=DEFAULT_FONT_STYLE, fg=LABEL_COLOR,
                              command=lambda: self.append_operator("-"))
        sub_operator.grid(row=3, column=4, sticky=NSEW)

        # row 0 and column 1
        clear_operator = Button(self.button_frame, text="C", bg=OFF_WHITE, font=DEFAULT_FONT_STYLE, fg=LABEL_COLOR,
                                command=self.clear)
        clear_operator.grid(row=0, column=1, sticky=NSEW)
        # row
        equals_operator = Button(self.button_frame, text="=", bg=LIGHT_BLUE, font=DEFAULT_FONT_STYLE, fg=LABEL_COLOR,
                                 command=self.evaluate_solution)
        equals_operator.grid(row=4, column=3, sticky=NSEW, columnspan=2)
        # creating square and square roots buttons
        square_button = Button(self.button_frame, text="x\u00b2", bg=OFF_WHITE, font=DEFAULT_FONT_STYLE, fg=LABEL_COLOR,
                                command=self.square)
        square_button.grid(row=0, column=2, sticky=NSEW)

        square_root_button = Button(self.button_frame, text="\u221ax", bg=OFF_WHITE, font=DEFAULT_FONT_STYLE, fg=LABEL_COLOR,
                               command=self.square_root)
        square_root_button.grid(row=0, column=3, sticky=NSEW)

    def run(self):
        self.window.mainloop()


calculator_app = Calculator()
calculator_app.run()
