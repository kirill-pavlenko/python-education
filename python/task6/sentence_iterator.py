"""
This module implements Sentence container and Sentence iterator
"""


class SentenceIterator:
    """
    SentenceIterator class implements iteration protocol for Sentence class
    """
    def __init__(self, words):
        self.words = words
        self._request = 0

    def __len__(self):
        return len(self.words)

    def __iter__(self):
        return self

    def __next__(self):
        if self._request < len(self):
            self._request += 1
            return self.words[self._request - 1]
        raise StopIteration


class Sentence:
    """
    Sentence class that implements iterable. Iterates through given sentence
    """
    end_sentence_characters = '.?!'
    non_word_characters = end_sentence_characters + ',/-+)(;:\"<>1234567890-='

    def __init__(self, text: str):
        if isinstance(text, str):
            if text[-1] in self.end_sentence_characters:
                self.sentence = text
            else:
                raise ValueError('Argument is not a valid sentence')
        else:
            raise TypeError('Argument is not in string type')

    def __repr__(self):
        return f"<Sentence(words={len(self.words)}, other_chars={len(self.other_chars)})>"

    def __iter__(self):
        return SentenceIterator(self.words)

    def __getitem__(self, item):
        return self.words[item]

    def _words(self):
        return (word for word in self.words)

    @property
    def words(self):
        """Returns words of the sentence"""
        clear_sentence = self.sentence
        for char in self.other_chars:
            clear_sentence = clear_sentence.replace(char, '')
        return clear_sentence.split()

    @property
    def other_chars(self):
        """Returns non-word characters of the sentence"""
        return [character for character in self.sentence if character
                in self.non_word_characters]


try:
    Sentence(True)
except TypeError as exc:
    print(exc)

try:
    Sentence('True')
except ValueError as exc:
    print(exc)

my_sentence = Sentence('Some random sentence, I won\'t add anything to it.')
print(my_sentence)
print(my_sentence._words())
print(next(my_sentence._words()))
print(my_sentence.words)
print(my_sentence.other_chars)
print(my_sentence[0])
print(my_sentence[:])
for word in my_sentence:
    print(word)
