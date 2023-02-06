import customtkinter
from tkinter.font import Font

from src.gui.vocab_gui_statistics import VocabGuiStatistics
from src.gui.vocab_gui_train import VocabGuiTrain
from src.utility.vokabel_setup import Setup


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
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        root = customtkinter.CTk()  # create CTk window like the Tk window
        root.geometry("1280x720")
        root.title("Vokabeltrainer Menu")

        return root

    def destroy_root(self):
        self.root.destroy()

    def setup(self):
        font = Font(family="Segoe Print", size=25)
        label = customtkinter.CTkLabel(master=self.root, text="MENU", text_font=font)

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
        font2 = Font(family="Times", size=11, underline=True)

        lang_1_button = customtkinter.CTkButton(self.root, text=mode_1, text_font=Font(size=15), relief="raised",
                                                command=lambda: self.select_mode(0, (lang_1_button, lang_2_button)),
                                                width=80, height=10)  # lambda methode übergeben welche parameter brauch
        lang_2_button = customtkinter.CTkButton(self.root, text=mode_2, text_font=Font(size=15), relief="raised",
                                                command=lambda: self.select_mode(1, (lang_1_button, lang_2_button)),
                                                width=80, height=10)

        statistics_button = customtkinter.CTkButton(self.root, text_font=font2, text="statistics", relief="raised",
                                                    width=10, height=5, command=lambda: self.statistics(), text_color="white", fg_color="grey")

        lang_1_button.grid(row=1, column=2, padx='5', ipady=21, ipadx=25, sticky="n")
        lang_2_button.grid(row=2, column=2, padx='5', ipady=21, ipadx=25, sticky="n")
        statistics_button.grid(row=5, column=2, sticky="s")


        self.button_difficulty()

    def button_difficulty(self):

        diff_1_button = customtkinter.CTkButton(self.root, text="easy", text_font=Font(size=12),
                                                command=lambda: self.select_settings(0, (
                                                    diff_1_button, diff_2_button, diff_3_button)), width=10, height=2)
        diff_2_button = customtkinter.CTkButton(self.root, text="normal", text_font=Font(size=12),
                                                command=lambda: self.select_settings(1, (
                                                    diff_2_button, diff_1_button, diff_3_button)), width=10, height=2)
        diff_3_button = customtkinter.CTkButton(self.root, text="hard", text_font=Font(size=12),
                                                command=lambda: self.select_settings(2, (
                                                    diff_3_button, diff_2_button, diff_1_button)), width=10, height=2)

        diff_1_button.grid(row=4, column=1, ipady=12, ipadx=15)
        diff_2_button.grid(row=4, column=2, ipady=12, ipadx=15)
        diff_3_button.grid(row=4, column=3, ipady=12, ipadx=15)

    def select_settings(self, setting, button):
        self.settings = (setting, True)
        self.change_diff_color(button)

    def select_mode(self, mode, button):
        self.mode = mode
        self.change_lang_color(button)

    def change_lang_color(self, button):
        if self.mode == 0:
            button[0].configure(fg_color="blue")
            button[1].configure(fg_color="grey")
        else:
            button[1].configure(fg_color="blue")
            button[0].configure(fg_color="grey")

        self.destroy_children(self.check_selection())

    def change_diff_color(self, button):
        button[0].configure(bg="light blue")
        button[1].configure(bg="light grey")
        button[2].configure(bg="light grey")

        button[0].after(100,
                        lambda: self.destroy_children(self.check_selection()))  # lambda: fkt mit parameter übergeben

    def check_selection(self):
        return self.mode != -1 and self.settings[0] != -1

    def destroy_children(self, selected):
        if selected:
            for child in self.root.winfo_children():
                child.destroy()

            self.start_training()

    def start_training(self):
        VocabGuiTrain(self.file_path, self.root, self.mode, self.lang_mode, self.pairs, self.settings, )

    def statistics(self):
        VocabGuiStatistics(self.file_path)




# VocabGuiMenu("C:/Users/imman/Desktop/Desktop/python/vokabeltrainer/vokabeltrainer.txt")
