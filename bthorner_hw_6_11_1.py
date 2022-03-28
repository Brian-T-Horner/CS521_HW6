"""
Brian Horner
CS 521 - Summer 1
Date: 6/22/2021
Homework Problem: 6_11_1
This program creates a class called Sentence which has a sentence string
attribute. It comes with get_all_words, get_word, set_word, and str methods.
"""


class Sentence:

    def __init__(self, input_sentence=""):
        """Constructs Sentence instance with private attribute __input_sentence
        and string_with_punctuation for sentence recall."""
        self.__input_sentence = input_sentence
        # Stripping punctuation and assigning to editable_sentence attribute
        self.editable_sentence = "".join(char for char in
                                         self.__input_sentence if
                                         char.isalpha() or char == " ")

    def get_all_words(self):
        """Returns all words in Sentence instance in a list."""
        return [word for word in self.editable_sentence.strip().split()]

    def get_word(self, index):
        """This function returns the word from the Sentence class instance
        located at the index specified"""
        self.index = index
        # Creating list out of sentence
        self.sentence_list = [word for word in self.editable_sentence.strip(
        ).split()]
        # Returning word in specified index
        return self.sentence_list[index]

    def set_word(self, index, new_word):
        """Replaces from the Sentence instance with a given word at a specified
        index."""
        # Initializing attributes
        self.index = index
        self.new_word = new_word
        # Creating list from sentence
        self.sentence_list = [word for word in self.editable_sentence.strip(
        ).split()]
        # Replacing word at specified index with new_word
        self.sentence_list[self.index] = self.new_word
        # Rejoining list into string sentence
        self.editable_sentence = " ".join(self.sentence_list)

    def __str__(self):
        """Returns original and modified sentence when print is called on
        instance."""
        return f"Your sentence original sentence was: \"" \
               f"{self.__input_sentence}\" \n" \
               f"Your modified sentence is: " \
               f"\"{self.editable_sentence}\""


if __name__ == "__main__":

    """ Unit Tests"""

    # Establishing user_sentence variable
    user_sentence = "Moving side to side, up and down like a rollercoaster."
    # Instantiate the Sentence object and checking type
    user_sentence = Sentence(user_sentence)
    print(type(user_sentence))
    # Printing the original sentence
    print(user_sentence)
    # Testing that get_all_words returns all words in a sentence
    print(user_sentence.get_all_words())
    # Testing that get_word gets the right word
    print(user_sentence.get_word(0))
    # Testing that set_word replaces the right word with the new one
    user_sentence.set_word(4, 'hi')

    # Returning original and modified sentence
    print(user_sentence)
