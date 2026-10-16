"""
OFFLINE DSA LAB EXAM PRACTICE
Save this file as modification_practice.py in the SAME folder as:
dictionary_index.py, bst_index.py, trie_index.py, and line_list.py.

Run:
    python modification_practice.py

This file does not modify your submitted project files.
"""

import re
import sys
import time

from dictionary_index import DictionaryIndex
from bst_index import BSTIndex
from trie_index import TrieIndex


def choose_index():
    """Ask which existing indexing implementation to use."""
    print("\nChoose the data structure:")
    print("1. Dictionary")
    print("2. Binary Search Tree (BST)")
    print("3. Trie")

    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        return DictionaryIndex(), "Dictionary"
    if choice == "2":
        return BSTIndex(), "BST"
    if choice == "3":
        return TrieIndex(), "Trie"

    print("Invalid choice. Using Dictionary.")
    return DictionaryIndex(), "Dictionary"


def tokenize(line):
    """
    Convert text to lowercase and extract words.
    Examples: 'Hello,' -> 'hello'; "WORLD!" -> 'world'.
    """
    return re.findall(r"[A-Za-z0-9_]+", line.lower())


def build_practice_index(filename, index):
    """
    Build the index using the existing add_word() method.
    Also return word frequencies and the total number of word occurrences.
    """
    frequencies = {}
    total_words = 0

    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            for word in tokenize(line):
                index.add_word(word, line_number)
                frequencies[word] = frequencies.get(word, 0) + 1
                total_words += 1

    return frequencies, total_words


def count_bst_nodes(node):
    """Count BST nodes recursively."""
    if node is None:
        return 0
    return 1 + count_bst_nodes(node.left) + count_bst_nodes(node.right)


def trie_prefix_search(trie, prefix):
    """Return complete words beginning with a prefix and their line numbers."""
    prefix = prefix.lower()
    current = trie.root

    for character in prefix:
        if character not in current.children:
            return []
        current = current.children[character]

    matches = []

    def collect(node, current_word):
        if node.line_numbers is not None:
            matches.append((current_word, node.line_numbers.get_lines()))

        for character in sorted(node.children):
            collect(node.children[character], current_word + character)

    collect(current, prefix)
    return matches

