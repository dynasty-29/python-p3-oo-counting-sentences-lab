import re

class MyString:
    def __init__(self, value=""):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")  # Fix: Raise an error instead of print

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")  # Fix: Raise error instead of print

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        sentences = re.split(r'[.!?]', self._value.strip())
        sentences = [s for s in sentences if s.strip()]  # Remove empty strings
        return len(sentences)
