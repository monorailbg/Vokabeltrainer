import os.path
import tkinter
from pathlib import Path
from tkinter import filedialog

from src.gui.vocab_gui_menu import VocabGuiMenu


class VocabGuiSelect:

    def __init__(self):
        self.fav_path = str(Path.home()) + "/vocableset1.txt"

        fav_path = self.get_fav_path()
        if fav_path != "":
            VocabGuiMenu(fav_path)
            exit(0)

        self.root: tkinter.Tk = self.create_root()
        self.setup()

    def create_root(self):
        root = tkinter.Tk()
        root.title("Vokabeltrainer")
        root.geometry("720x480")
        root.configure(bg="white")
        return root

    def destroy_root(self):
        self.root.destroy()

    def setup(self):
        tkinter.Button(self.root, text="Select vocable dataset", bg="white", command=self.select_vocab_dataset).pack(pady=200)
        self.root.mainloop()

    def select_vocab_dataset(self):
        file_types = (
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        )
        file_path = filedialog.askopenfilename(
            title="select vocable dataset",
            initialdir="/",
            filetypes=file_types
        )
        self.save_fav_path(file_path)
        self.destroy_root()

        VocabGuiMenu(file_path)

    def save_fav_path(self, path):
        file = open(self.fav_path, "w")
        file.write(path)

    def get_fav_path(self):
        if not os.path.exists(self.fav_path):
            return ""

        file = open(self.fav_path, "r")
        return file.read()

VocabGuiSelect()
