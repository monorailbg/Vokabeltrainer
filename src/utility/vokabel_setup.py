import random as rand

from src.models.vokabel import Vokabel


class Setup:

    def __init__(self):  # konstruktor
        print("")

    def read_text_file(self, path):
        lines = []  # array
        with open(path) as file:
            language = file.readline()  # string
            lines = file.readlines()  # array
            rand.shuffle(lines)
        return lines, language  # tupel

    def get_vocables(self, lines, language):
        vocables = []  # Array von Vokabeln

        language_a = language.split("/")[0]
        language_b = language.split("/")[1]

        for line in lines:
            line = line.replace("\n", "").replace(" ", "")

            vocable_idx = line.split("-")[0]
            text_a = line.split("-")[1]
            text_b = line.split("-")[2]

            vocable = Vokabel(vocable_idx, text_a, text_b, language_a, language_b)  # Datentyp = Vokabel

            vocables.append(vocable)

        return vocables  # Array aus Vokabeln

    def select_mode(self, language):
        language_a = language.split("/")[0]  # string, ein element wird entnommen
        language_b = language.split("/")[1].replace("\n", "")  # string
        print("Select mode\n")
        print("1 - ", language_a, "/", language_b)
        print("2 - ", language_b, "/", language_a)
        mode = int(input())  # int
        if 0 < mode < 3:
            return mode, language_a, language_b  # tupel

        return self.select_mode(language)

    def get_lang(self, language):
        language_a = language.split("/")[0]  # string, ein element wird entnommen
        language_b = language.split("/")[1].replace("\n", "")  # string

        return language_a, language_b

    def mode_1(self, language):
        language_a = language.split("/")[0]  # string, ein element wird entnommen
        language_b = language.split("/")[1].replace("\n", "")  # string

        return language_a + "/" + language_b

    def mode_2(self, language):
        language_a = language.split("/")[0]  # string, ein element wird entnommen
        language_b = language.split("/")[1].replace("\n", "")  # string

        return language_b + "/" + language_a

    def setup_settings(self):
        difficulty = input("Please select difficulty (easy, normal, hard)\n")  # string

        if difficulty != "easy" and difficulty != "normal" and difficulty != "hard":
            return self.setup_settings()
        is_rated = input("Please choose if the test should be rated (true, false)\n") == "true"  # boolean

        return difficulty, is_rated  # tupel
