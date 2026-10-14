import sys
from dictionary_index import DictionaryIndex
from bst_index import BSTIndex
from trie_index import TrieIndex


# Read the input file and store each word with its line number
def build_index(input_filename, index):

    # Open the input file in read mode
    with open(input_filename, "r", encoding="ascii") as file:

        # Start counting lines from 1
        line_number = 1

        # Read the file one line at a time
        for line in file:

            # Start with an empty word
            word = ""

            # Read each character in the current line
            for character in line:

                # Check whether the character is a word separator
                if character in " \n.,:;":

                    # Store the word if it is not empty
                    if word != "":
                        index.add_word(word, line_number)

                        # Reset the word for the next word
                        word = ""

                else:
                    # Add the character to the current word
                    word += character

            # Store the last word in the line, if any
            if word != "":
                index.add_word(word, line_number)

            # Move to the next line number
            line_number += 1

    # Return the completed index
    return index


# Get filenames and search word from command-line arguments
input_filename = sys.argv[1]
output_filename = sys.argv[2]
# search_word = sys.argv[3]

# Create a Trie to store the index
index = TrieIndex()

# Build the index using the input file
build_index(input_filename, index)

# Write the complete index to the output file
index.print_index(output_filename)

# Search for the requested word
# result = index.search(search_word)

# Check whether the word exists in the index
# if result is None:
#     print("Word not found")
# else:
#     # Display the word and its line numbers
#     print("Word:", search_word)
#     print("Line numbers:", result)
