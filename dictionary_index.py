
# Create an index using a Python dictionary
from line_list import LineList

class DictionaryIndex:

    def __init__(self):
        # Create an empty dictionary to store words and line numbers
        self.index = {}

    # Add a word and its line number to the index
    def add_word(self, word, line_number):

        # Check whether the word is already in the dictionary
        if word not in self.index:

            # Create an empty list for a new word
            self.index[word] = LineList()

        # Add the line number to the word's list
        self.index[word].add(line_number)

    # Search for a word and return its line numbers
    def search(self, word):
        if word in self.index:
            return self.index[word].get_lines()
        return None

    # Write the complete index to an output file
    def print_index(self, filename):
        with open(filename, "w", encoding="ascii") as file:
            for word in sorted(self.index):
                file.write(word + " -> ")
                for line_number in self.index[word].get_lines():
                    file.write(str(line_number) + " ")
                file.write("\n")

