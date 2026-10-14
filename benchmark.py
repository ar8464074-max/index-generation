
import time
import random
import sys
import csv

from dictionary_index import DictionaryIndex
from bst_index import BSTIndex
from trie_index import TrieIndex


# Store the benchmark results of all three data structures
results = []


# Read the input file and store each word with its line number
def build_index(input_filename, index):

    # Open the input file in read mode
    with open(input_filename, "r", encoding="ascii") as file:
        line_number = 1

        # Read the file one line at a time
        for line in file:
            word = ""

            # Read each character in the current line
            for character in line:

                # Check whether the character separates words
                if character in " \n.,:;":

                    # Add the word if it is not empty
                    if word != "":
                        index.add_word(word, line_number)
                        word = ""

                else:
                    # Build the word one character at a time
                    word += character

            # Add the last word in the line
            if word != "":
                index.add_word(word, line_number)

            # Move to the next line
            line_number += 1


# Read all words from the input file into a list
def get_words(input_filename):
    words = []

    # Open the input file in read mode
    with open(input_filename, "r", encoding="ascii") as file:

        # Process one line at a time
        for line in file:
            word = ""

            # Read each character in the line
            for character in line:

                # Check for a word separator
                if character in " \n.,:;":

                    # Save the completed word
                    if word != "":
                        words.append(word)
                        word = ""

                else:
                    # Add the character to the current word
                    word += character

            # Save the last word in the line
            if word != "":
                words.append(word)

    # Return the list of words
    return words


# Check whether the input filename was provided
if len(sys.argv) < 2:
    print("Usage: python benchmark.py input_filename")
    sys.exit()


# Get the input filename from the command line
input_filename = sys.argv[1]

# Read all words from the file
words = get_words(input_filename)

# Randomly select 100,000 words for searching
search_words = random.choices(words, k=100000)


# ---------------- Dictionary Benchmark ----------------

# Create an empty dictionary-based index
dictionary = DictionaryIndex()

# Measure the time required to build the index
start = time.perf_counter()
build_index(input_filename, dictionary)
dictionary_construction_time = time.perf_counter() - start

# Measure the time required to search 100,000 words
start = time.perf_counter()

for word in search_words:
    dictionary.search(word)

dictionary_search_time = time.perf_counter() - start

# Measure the time required to write the index to a file
start = time.perf_counter()
dictionary.print_index("dictionary_output.txt")
dictionary_printing_time = time.perf_counter() - start

# Display the dictionary benchmark results
print("Dictionary")
print("Construction time:", dictionary_construction_time)
print("Search time:", dictionary_search_time)
print("Printing time:", dictionary_printing_time)

# Store the dictionary results for the CSV file
results.append([
    input_filename,
    "Dictionary",
    dictionary_construction_time,
    dictionary_search_time,
    dictionary_printing_time
])


# ---------------- BST Benchmark ----------------

# Create an empty Binary Search Tree index
bst = BSTIndex()

# Measure the time required to build the BST
start = time.perf_counter()
build_index(input_filename, bst)
bst_construction_time = time.perf_counter() - start

# Measure the time required to search 100,000 words
start = time.perf_counter()

for word in search_words:
    bst.search(word)

bst_search_time = time.perf_counter() - start

# Measure the time required to print the BST index
start = time.perf_counter()
bst.print_index("bst_output.txt")
bst_printing_time = time.perf_counter() - start

# Display the BST benchmark results
print("\nBST")
print("Construction time:", bst_construction_time)
print("Search time:", bst_search_time)
print("Printing time:", bst_printing_time)

# Store the BST results for the CSV file
results.append([
    input_filename,
    "BST",
    bst_construction_time,
    bst_search_time,
    bst_printing_time
])


# ---------------- Trie Benchmark ----------------

# Create an empty Trie index
trie = TrieIndex()

# Measure the time required to build the Trie
start = time.perf_counter()
build_index(input_filename, trie)
trie_construction_time = time.perf_counter() - start

# Measure the time required to search 100,000 words
start = time.perf_counter()

for word in search_words:
    trie.search(word)

trie_search_time = time.perf_counter() - start

# Measure the time required to print the Trie index
start = time.perf_counter()
trie.print_index("trie_output.txt")
trie_printing_time = time.perf_counter() - start

# Display the Trie benchmark results
print("\nTrie")
print("Construction time:", trie_construction_time)
print("Search time:", trie_search_time)
print("Printing time:", trie_printing_time)

# Store the Trie results for the CSV file
results.append([
    input_filename,
    "Trie",
    trie_construction_time,
    trie_search_time,
    trie_printing_time
])


# ---------------- Save Benchmark Results ----------------

# Open the CSV file in append mode
with open("benchmark_results.csv", "a", newline="") as file:

    # Create a CSV writer to save rows
    writer = csv.writer(file)

    # Write the column headings if the file is empty
    if file.tell() == 0:
        writer.writerow([
            "File",
            "Method",
            "Construction Time",
            "Search Time",
            "Printing Time"
        ])
     
    # Write the results of all three data structures
    for result in results:
        writer.writerow(result)
