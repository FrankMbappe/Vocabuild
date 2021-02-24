from src.modules.level import Level
from src.modules.word import Word
import random


def get_a_suitable_word(word_list, picked_words_list, level, max_picks):
    randomWord = random.choice(word_list)
    print(f"Word initially generated: {randomWord}")

    for i in range(len(word_list)):
        if (randomWord in picked_words_list and randomWord.number_of_time_picked() > max_picks) \
                or not randomWord.level_is_suitable(level):
            randomWord = random.choice(word_list)
        else:
            picked_words_list.append(randomWord)
            return randomWord.pick()

    return None


words = [
    Word(
        value='Gate',
        definition='A point of entry to a space enclosed by walls',
        level=Level.Medium
    ),
    Word(
        value='Keyboard',
        definition='A typewriter-style device which uses an arrangement of buttons or keys to act as mechanical '
                   'levers or electronic switches',
        level=Level.Advanced
    ),
    Word(
        value='Screen',
        definition='An output device that displays information in pictorial form. A monitor usually comprises the '
                   'visual display, circuitry, casing, and power supply',
        level=Level.Beginner
    )
]

pickedWords = []

word = get_a_suitable_word(
    word_list=words,
    picked_words_list=pickedWords,
    level=Level.Intermediate,
    max_picks=3
)

if word is not None:
    print(f"Word finally generated: {word}. It has been picked {word.number_of_time_picked()} time(s).")
else:
    print(f"No word has been generated.")
