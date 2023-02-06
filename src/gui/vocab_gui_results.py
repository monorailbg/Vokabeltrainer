from tkinter.font import Font

import customtkinter


class VocabGuiResults:

    def __init__(self, root, result):
        self.root = root
        self.correct_vocables = result[0]
        self.failed_vocables = result[1]
        self.configure()
        self.create_interface()

    def configure(self):
        self.root.grid_rowconfigure(0, weight=2)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(6, weight=1)

    def create_interface(self):
        font = Font(family="Segoe Print", size=16, weight="bold")
        label_title = customtkinter.CTkLabel(self.root, text="You finished your set!", text_font=font)
        label_title.grid(row=0, column=2)
        self.label_result = customtkinter.CTkLabel(self.root, text="", bg="white")
        self.label_result.grid(row=2, column=2)
        self.set_text()
        self.home_button()

    def set_text(self):
        self.vocable_length = len(self.correct_vocables) + len(self.failed_vocables)
        self.label_result.configure(text= "You achieved " + str(len(self.correct_vocables)) + " out of " + str(self.vocable_length) + " correct")

    def home_button(self):
        home_button = customtkinter.CTkButton(self.root, text="Return to Menu", command=self.return_to_menu)
        home_button.grid(row=4, column=2)

    def return_to_menu(self):
        self.root.destroy()
        quit(0)

    def save_results(self, failed_vocables, correct_vocables):
        print(failed_vocables, correct_vocables)
