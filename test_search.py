
# Import the three index implementations
from dictionary_index import DictionaryIndex
from bst_index import BSTIndex
from trie_index import TrieIndex


# Test searching for existing and missing words
def test_search(index):

    # Search for a word that appears on two lines
    print("Search: hello")
    print(index.search("hello"))

    # Search for a word that appears on one line
    print("Search: world")
    print(index.search("world"))

    # Search for a word that does not exist
    print("Search: xyz")
    print(index.search("xyz"))


# ---------------- Test Dictionary ----------------

print("DICTIONARY")

# Create an empty dictionary-based index
dictionary = DictionaryIndex()

# Add words with their line numbers
dictionary.add_word("hello", 1)
dictionary.add_word("world", 1)
dictionary.add_word("hello", 2)

# Run the search tests on the dictionary
test_search(dictionary)


# ---------------- Test BST ----------------

print("\nBST")

# Create an empty Binary Search Tree index
bst = BSTIndex()

# Add words with their line numbers
bst.add_word("hello", 1)
bst.add_word("world", 1)
bst.add_word("hello", 2)

# Run the search tests on the BST
test_search(bst)


# ---------------- Test Trie ----------------

print("\nTRIE")

# Create an empty Trie index
trie = TrieIndex()

# Add words with their line numbers
trie.add_word("hello", 1)
trie.add_word("world", 1)
trie.add_word("hello", 2)

# Run the search tests on the Trie
test_search(trie)
