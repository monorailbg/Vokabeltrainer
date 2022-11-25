import time
import tkinter
from tkinter.font import Font

from src.gui.vocab_gui_train import VocabGuiTrain
from src.vokabel_setup import Setup


class VocabGuiMenu:

    def __init__(self, file_path):
        self.file_path = file_path
        self.settings = (-1, True)
        self.root = self.create_root()
        self.mode = -1
        self.language = ""
        self.lang_mode = ""
        self.pairs = []

        self.setup()

    def create_root(self):
        root = tkinter.Tk()
        root.title("Vokabeltrainer")
        root.geometry("720x480")
        root.config(bg="white")

        return root

    def destroy_root(self):
        self.root.destroy()

    def setup(self):
        font = Font(family="Segoe Print", size=20)
        label = tkinter.Label(self.root, text="MENU", font=font, bg="white")

        label.grid(row=0, pady=0, column=2)

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

        self.add_buttons()

        self.root.mainloop()

    def add_buttons(self):

        setup = Setup()
        lines_tuple = setup.read_text_file(self.file_path)
        self.language = lines_tuple[1]
        self.pairs = setup.get_vocables(lines_tuple[0], self.language)
        self.lang_mode = setup.get_lang(self.language)

        mode_1 = setup.mode_1(self.language)
        mode_2 = setup.mode_2(self.language)

        lang_1_button = tkinter.Button(self.root, text=mode_1, command=lambda: self.select_mode(0, (lang_1_button, lang_2_button)), width=20, height=2) #lambda methode übergeben welche parameter brauch
        lang_2_button = tkinter.Button(self.root, text=mode_2, command=lambda: self.select_mode(1, (lang_1_button, lang_2_button)), width=20, height=2)

        lang_1_button.grid(row=1, column=2, padx='5', ipady=10, sticky="n")
        lang_2_button.grid(row=2, column=2, padx='5', ipady=10, sticky="n")
        self.button_difficulty()

    def button_difficulty(self):
        diff_1_button = tkinter.Button(self.root, text="easy", command=lambda: self.select_settings(0, (diff_1_button, diff_2_button, diff_3_button)), width=10, height=2)
        diff_2_button = tkinter.Button(self.root, text="normal", command=lambda: self.select_settings(1, (diff_2_button, diff_1_button, diff_3_button)), width=10, height=2)
        diff_3_button = tkinter.Button(self.root, text="hard", command=lambda: self.select_settings(2, (diff_3_button, diff_2_button, diff_1_button)), width=10, height=2)

        diff_1_button.grid(row=4, column=1)
        diff_2_button.grid(row=4, column=2)
        diff_3_button.grid(row=4, column=3)

    def select_settings(self, setting, button):
        self.settings = (setting, True)
        self.change_diff_color(button)

    def select_mode(self, mode, button: tkinter.Button):
        self.mode = mode
        self.change_lang_color(button)

    def change_lang_color(self, button):
        if self.mode == 0:
            button[0].config(bg="light blue")
            button[1].config(bg="light grey")
        else:
            button[1].config(bg="light blue")
            button[0].config(bg="light grey")

        self.destroy_children(self.check_selection())

    def change_diff_color(self, button):
        button[0].config(bg="light blue")
        button[1].config(bg="light grey")
        button[2].config(bg="light grey")

        button[0].after(100, lambda: self.destroy_children(self.check_selection())) #lambda: fkt mit parameter übergeben

    def check_selection(self):
        return self.mode != -1 and self.settings[0] != -1

    def destroy_children(self, selected):
        if selected:
            for child in self.root.winfo_children():
                child.destroy()

            self.start_training()

    def start_training(self):
        VocabGuiTrain(self.root, self.mode, self.lang_mode, self.pairs, self.settings)


#VocabGuiMenu("C:/Users/imman/Desktop/Desktop/python/vokabeltrainer/vokabeltrainer.txt")
