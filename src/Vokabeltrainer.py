from src.input.vokabel import Vokabel
from src.vokabel_setup import Setup

vocab_path = "C:\\Users\\imman\\PycharmProjects\\Vokabeltrainer\\src\\input\\vokabeltrainer.txt"


def start_training(vocables, training_mode, training_settings):
    if training_mode[0] == 1:  # Lang A to Lang B
        training_lang = training_mode[2]  # string
    else:  # Lang B to Lang A
        training_lang = training_mode[1]  # string

    print("\nPlease give the", training_lang, "translation for the given words\n")

    training(vocables, training_mode[0], training_settings)


def training(vocables, mode, training_settings):
    failed_vocables = []  # array
    correct_vocables = []  # array

    voc: Vokabel
    for voc in vocables:  # Vokabel

        if mode == 1:
            text = input("word: " + voc.text_a + "> ")
        else:
            text = input("word: " + voc.text_b + "> ")

        if mode == 1:
            if text == voc.text_b:
                correct_vocables.append(voc)
            else:
                failed_vocables.append(voc)
        else:
            if text == voc.text_a:
                correct_vocables.append(voc)
            else:
                failed_vocables.append(voc)

    if training_settings[1]:  # boolean von setupSettings, [1] -> isRated
        print("You answered", len(correct_vocables), "out of", len(vocables), "correct")

    save_results(failed_vocables, correct_vocables)


def save_results(failed_vocables, correct_vocables):
    print(failed_vocables, correct_vocables)

"""
setup = Setup()

lines_tuple = setup.read_text_file(vocab_path)  # tupel
language = lines_tuple[1]  # string
pairs = setup.get_vocables(lines_tuple[0], language)  # Arrays aus Vokablen
mode = setup.select_mode(language)  # tupel
settings = setup.setup_settings()  # tupel
start_training(pairs, mode, settings)
"""
