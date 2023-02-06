import customtkinter
from tkinter.font import Font

from src.models.stats import Stats


class VocabGuiStatistics:

    def __init__(self, file_path): #self -> globale variable für die class
        self.root = customtkinter.CTk()
        self.setup_tkinter()
        self.path = file_path
        self.load_statistics()

    def setup_tkinter(self):
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        self.root.geometry("1280x720")
        self.root.title("Statistics")
        self.root.mainloop()

    def load_statistics(self):
        stats = Stats()
        statistics = stats.load()
        print (statistics)
