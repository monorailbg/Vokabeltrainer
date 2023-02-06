import os
import json


class Stats:
    save_path = '%s\\Vokabeltrainer\\' % os.environ['APPDATA']  # string
    file_path = '%sstats.json' % save_path  # string

    def __init__(self, index=-1, path="", mode_a_correct=0, mode_b_correct=0, mode_a_wrong=0, mode_b_wrong=0, ):

        self.index = index
        self.mode_a_correct = mode_a_correct
        self.mode_b_correct = mode_b_correct
        self.mode_a_wrong = mode_a_wrong
        self.mode_b_wrong = mode_b_wrong
        self.path = path

        if index == -1:
            return

        self.create_path()

    def counter(self, stat, mode, correct):
        if type(stat) != dict:
            stat = stat.__dict__

        if mode == 0 and correct:
            stat['mode_a_correct'] += 1
        elif mode == 0 and not correct:
            stat['mode_a_wrong'] += 1
        elif mode == 1 and correct:
            stat['mode_b_correct'] += 1
        else:
            stat['mode_b_wrong'] += 1
        return stat

    def create_path(self):
        if not os.path.exists(self.save_path):  # boolean
            os.makedirs(self.save_path)  # boolean

    def load(self):
        stats = []  # array
        if not os.path.isfile(self.file_path):
            return stats
        with open(self.file_path, "r") as file:
            stats = json.load(file)
        return stats

    def save(self, old_stat, current_stat):
        stats = self.load()

        if type(old_stat) != dict:
            old_stat = old_stat.__dict__

        if type(current_stat) != dict:
            current_stat = current_stat.__dict__

        old_stat_index = self.get_list_index(old_stat['index'])

        if old_stat_index == -1:
            stats.append(current_stat)
        else:
            stats[old_stat_index] = current_stat

        with open(self.file_path, "w") as file:  # with schließt datei automatisch
            file.write(json.dumps(stats, default=vars, sort_keys=True))

    def stats_exist(self, stats):
        for stat in stats:
            if stat.index == self.index:
                return True
        return False

    def get_list_index(self, index):
        stats = self.load()
        count = 0
        for stat in stats:
            if stat['index'] == index:
                return count
            else:
                count += 1
        return -1

    def find_stat(self, index, path):
        stats = self.load()

        for stat in stats:  # datentyp: stats
            if stat['index'] == index and stat['path'] == path:
                return stat

        self.index = index
        self.path = path

        return self


"""

Vokablen;
12 - pear - Birne
4 - consequence - Folge
46 - spider - Spinne
34 - apple - Apfel
24 - country - Land
....
.....


Liste

0 - (index = 12, mode_a_correct = 3, mode_b_correct = 2, ...)
1 - (index = 4, mode_a_correct = 4, mode_b_correct = 2, ...)
2 - (index = 46, mode_a_correct = 13, mode_b_correct = 2, ...)
3 - (index = 34, mode_a_correct = 23, mode_b_correct = 2, ...)
4 - (index = 64, mode_a_correct = 43, mode_b_correct = 2, ...)
5 - (index = 24, mode_a_correct = 32, mode_b_correct = 2, ...) 
6 - (index = 53, mode_a_correct = 13, mode_b_correct = 2, ...) 
7 - (index = 5, mode_a_correct = 33, mode_b_correct = 2, ...)



"""
