
from line_list import LineList


# Create a node for each character in the Trie
class TrieNode:

    def __init__(self):
        # Store the next characters connected to this node
        self.children = {}

        # Store line numbers only when a complete word ends here
        self.line_numbers = None


# Create a Trie-based index
class TrieIndex:

    def __init__(self):
        # Create the root node of the Trie
        self.root = TrieNode()

    # Add a word and its line number to the Trie
    def add_word(self, word, line_number):

        # Start from the root node
        current = self.root

        # Process each character in the word
        for character in word:

            # Create a new node if the character does not exist
            if character not in current.children:
                current.children[character] = TrieNode()

            # Move to the node for the current character
            current = current.children[character]

        # Create a line-number list if this is a new word
        if current.line_numbers is None:
            current.line_numbers = LineList()

        # Store the line number for this word
        current.line_numbers.add(line_number)

    # Search for a word and return its line numbers
    def search(self, word):

        # Start searching from the root
        current = self.root

        # Follow the characters of the search word
        for character in word:

            # Return None if a character path does not exist
            if character not in current.children:
                return None

            # Move to the next character node
            current = current.children[character]

        # Check whether a complete word ends at this node
        if current.line_numbers is not None:
            return current.line_numbers.get_lines()

        # Return None if the complete word does not exist
        return None

    # Write all words in lexicographical order
    def _write_words(self, node, prefix, file):

        # If a complete word ends here, write it to the file
        if node.line_numbers is not None:

            # Write the word followed by an arrow
            file.write(prefix + " -> ")

            # Write all line numbers associated with the word
            for line_number in node.line_numbers.get_lines():
                file.write(str(line_number) + " ")

            # Move to the next line in the output file
            file.write("\n")

        # Visit child characters in sorted order
        for character in sorted(node.children):

            # Continue traversing with the updated word prefix
            self._write_words(
                node.children[character],
                prefix + character,
                file
            )

    # Save the complete index to an output file
    def print_index(self, filename):

        # Open the output file in write mode
        with open(filename, "w", encoding="ascii") as file:

            # Start writing words from the root node
            self._write_words(self.root, "", file)
