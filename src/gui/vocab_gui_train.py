import asyncio
from tkinter import StringVar
from tkinter.font import Font
from tkinter.ttk import Style

import customtkinter

from src.gui.vocab_gui_results import VocabGuiResults
from src.models.stats import Stats


class VocabGuiTrain:

    def __init__(self, path, root, mode, language, vocables, settings):
        self.root: customtkinter.CTk = root
        self.mode = mode
        self.settings = settings
        self.language = language
        self.vocables = vocables
        self.settings = settings
        self.label_word = ""
        self.entry_word = StringVar()
        self.configure()
        self.vocable_length = len(vocables)
        self.correct_vocables = []
        self.failed_vocables = []
        self.remaining_vocables = []
        self.path = path
        self.percent = StringVar()
        self.percent_label: customtkinter.CTkLabel
        self.progress_bar_1: customtkinter.CTkProgressBar
        self.progress_bar_2: customtkinter.CTkProgressBar
        self.create_interface()

        self.ask_vocable()
        asyncio.run(self.start_progress_bar())

    def configure(self):
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)

        self.root.grid_rowconfigure(0, weight=2)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(6, weight=1)

    def create_interface(self):
        label_title = customtkinter.CTkLabel(self.root, text=self.get_title_text(),
                                             text_font=Font(family="Segoe Print", size=10, weight="bold"))
        label_title.grid(row=0, pady=10, column=2, sticky="n")
        self.label_word = customtkinter.CTkLabel(self.root, text="",
                                                 text_font=Font(family="Segoe Print", size=10, weight="bold"))
        self.label_word.grid(row=1, column=2, sticky="n")
        entry_word = customtkinter.CTkEntry(self.root, textvariable=self.entry_word)
        entry_word.grid(row=1, column=2)
        entry_word.bind("<Return>", self.enter_button)  # mit klammer wird methode ausgeführt, ohne erst mit bedingung
        completed = customtkinter.CTkButton(self.root, text="completed", command=self.complete_vocable)
        completed.grid(row=2, column=2)

        self.setup_progress_bar()

    def difficulty_seconds(self):
        difficulty = self.settings[0]
        if difficulty == 0:
            return 60
        elif difficulty == 1:
            return 40
        else:
            return 20

    async def start_progress_bar(self):
        sec = self.difficulty_seconds()
        self.progress_bar_1.set(0)
        self.progress_bar_2.set(0)

        speed = 1

        ms = 0

        try:
            while sec > speed:
                await asyncio.sleep(0.001)
                ms += 1

                if ms == 65:
                    ms = 0
                    self.progress_bar_1.step()
                    self.progress_bar_2.step()

                    self.percent.set(str(sec - speed) + "s")

                    speed += 1

                self.root.update()
        except Exception:
            print("keyboard interrupted!")

        self.failed_vocables += self.vocables
        self.finish()

    def setup_progress_bar(self):  # alle methoden u. variablen in self gespeichert, verweis auf klasse
        style = Style()

        style.theme_use("clam")
        style.configure(style="bar.Vertical.TProgressbar", corner_radius="default_theme", fg_color="default_theme",
                        bg_color="black", border_color="default_theme", troughcolor="white",
                        progress_color="default_theme", lightcolor="green")

        self.progress_bar_1 = customtkinter.CTkProgressBar(self.root, orient="vertical",
                                                           height=self.root.winfo_height(), width=20)
        self.progress_bar_1.grid(row=0, column=0, rowspan=6)

        self.progress_bar_2 = customtkinter.CTkProgressBar(self.root, orient="vertical",
                                                           height=self.root.winfo_height(), width=20)
        self.progress_bar_2.grid(row=0, column=3, rowspan=6, sticky="e")

        self.percent_label = customtkinter.CTkLabel(self.root, textvariable=self.percent, background="white",
                                                    text_font=Font(family="Segoe Print", size=15))
        self.percent_label.grid(row=5, column=2)

    def get_title_text(self):
        if self.mode == 1:  # Lang A to Lang B
            training_lang = self.language[1]  # string
        else:  # Lang B to Lang A
            training_lang = self.language[0]  # string

        return "\nPlease give the " + training_lang + " translation for the given words\n"

    def ask_vocable(self):
        voc = self.vocables[0]

        if self.mode == 1:
            text = "word: " + voc.text_a
        else:
            text = "word: " + voc.text_b

        self.label_word.configure(text=text)
        self.entry_word.set("")

    def enter_button(self, event):
        self.complete_vocable()

    def complete_vocable(self):
        stats = Stats()  # instanziieren

        vocable_stat = stats.find_stat(self.vocables[0].idx, self.path)  # if fails, standard statistic is created
        temp_old_vocable = vocable_stat  # temporary vocable

        if self.mode == 1:
            text = self.vocables[0].text_b
        else:
            text = self.vocables[0].text_a

        if text == self.entry_word.get():
            self.correct_vocables.append(self.vocables[0])
            vocable_stat = stats.counter(vocable_stat, self.mode, True)
        else:
            self.failed_vocables.append(self.vocables[0])
            vocable_stat = stats.counter(vocable_stat, self.mode, False)

        stats.save(temp_old_vocable, vocable_stat)
        self.vocables.pop(0)

        if len(self.vocables) > 0:
            self.ask_vocable()
        else:
            self.finish()

    def finish(self):
        self.destroy_children(True)
        VocabGuiResults(self.root, (self.correct_vocables, self.failed_vocables))


    def destroy_children(self, selected):
        if selected:
            for child in self.root.winfo_children():
                child.destroy()
