from random import shuffle
import random as r


class Anagram:
    def __init__(self, word):
        self.word = list(word)

    def anagram(self):
        r.shuffle(self.word)
        return ''.join(self.word)


new_word = Anagram(str(input('Input key:')))
print(new_word.anagram())
