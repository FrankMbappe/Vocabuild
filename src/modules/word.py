from datetime import datetime
from src.modules.level import Level
from src.modules.pick import Pick


class Word:
    # Each time a word will be picked, that operation will be stored in this list
    pick_history = list()

    def __init__(self, value, definition, level):
        self.value = value
        self.definition = definition
        self.level = level

    def __str__(self):
        return f"'{self.value}', Level: {Level(self.level).name}"

    '''
        Pick a word
    '''
    def pick(self):
        self.pick_history.append(Pick(datetime.now()))
        return self

    '''
        The number of picks in the pick history
    '''
    def number_of_time_picked(self):
        return len(self.pick_history)

    def level_is_suitable(self, level):
        return int(self.level) in [int(level) - 1, int(level), int(level) + 1]
