INDEX GENERATION PROJECT
README

1. PROJECT DESCRIPTION

This project generates a word index from a text file.

The project implements the index using three different data structures:

1. Python Dictionary
2. Binary Search Tree (BST)
3. Trie

Each word is stored with a linked list of the line numbers where it occurs.


2. REQUIREMENTS

Python 3.x

Matplotlib is required for generating the performance graphs.

Install Matplotlib using:

python -m pip install matplotlib


3. RUNNING THE INDEX GENERATOR

The main utility accepts two command-line arguments:

python main.py input_filename output_filename

Example:

python main.py input.txt output.txt

The first argument is the input text file.

The second argument is the output file where the generated index is stored.


4. RUNNING SEARCH TESTS

Run:

python test_search.py

This tests searching in the Dictionary, BST, and Trie implementations.


5. PERFORMANCE BENCHMARK

The benchmark program accepts the input filename as an argument.

Example:

python benchmark.py file1.txt

The benchmark measures:

- Construction time
- Search time for 100,000 random words
- Printing time


6. SIX INPUT FILES

The project uses:

file1.txt  -> 1,000 distinct words
file2.txt  -> 5,000 distinct words
file3.txt  -> 10,000 distinct words
file4.txt  -> 50,000 distinct words
file5.txt  -> 100,000 distinct words
file6.txt  -> 500,000 distinct words

Each file contains more than one million words.


7. PERFORMANCE RESULTS

The benchmark results are stored in:

benchmark_results.csv


8. GENERATING GRAPHS

Run:

python plot_results.py

This generates three graphs:

construction_time.png
search_time.png
printing_time.png


9. MAIN SOURCE FILES

main.py
    Command-line utility for generating an index.

dictionary_index.py
    Dictionary-based implementation.

bst_index.py
    Binary Search Tree implementation.

trie_index.py
    Trie implementation.

line_list.py
    Linked list used to store line numbers.

test_search.py
    Test cases for the three implementations.

benchmark.py
    Performance measurement program.

plot_results.py
    Generates Matplotlib performance graphs.