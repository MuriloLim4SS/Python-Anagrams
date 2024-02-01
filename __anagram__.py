import random

class Anagram:
    def __init__(self, word):
        self.word = word
        self.word_list = None

    def anagram(self):
        self.word_list = []
        for i in self.word.split():
            self.word_list.append(i)

        shuffled_words = []
        for item in self.word_list:
            item = list(item)
            random.shuffle(item)
            item = ''.join(item)
            shuffled_words.append(item)

        print(' '.join(shuffled_words))

new_word = Anagram(str(input('Input key:')))
new_word.anagram()
