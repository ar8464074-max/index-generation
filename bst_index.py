
from line_list import LineList


# Create a node to store a word and its line numbers
class BSTNode:

    def __init__(self, word, line_number):
        # Store the word in this node
        self.word = word

        # Create a linked list to store line numbers
        self.line_numbers = LineList()

        # Add the first occurrence of the word
        self.line_numbers.add(line_number)

        # Initially, the node has no left or right child
        self.left = None
        self.right = None


# Create a Binary Search Tree to store the index
class BSTIndex:

    def __init__(self):
        # Initially, the tree is empty
        self.root = None

    # Add a word and its line number to the BST
    def add_word(self, word, line_number):

        # If the tree is empty, create the root node
        if self.root is None:
            self.root = BSTNode(word, line_number)
            return

        # Start searching from the root
        current = self.root

        # Continue until the word is inserted or found
        while True:

            # If the word already exists, add its line number
            if word == current.word:
                current.line_numbers.add(line_number)
                return

            # If the word is alphabetically smaller, go left
            elif word < current.word:

                # If the left child is empty, insert the new node
                if current.left is None:
                    current.left = BSTNode(word, line_number)
                    return

                # Otherwise, continue searching in the left subtree
                current = current.left

            # If the word is alphabetically greater, go right
            else:

                # If the right child is empty, insert the new node
                if current.right is None:
                    current.right = BSTNode(word, line_number)
                    return

                # Otherwise, continue searching in the right subtree
                current = current.right

    # Search for a word and return its line numbers
    def search(self, word):

        # Start searching from the root
        current = self.root

        # Continue until the word is found or the search ends
        while current is not None:

            # Return the line numbers if the word is found
            if word == current.word:
                return current.line_numbers.get_lines()

            # Search the left subtree if the word is smaller
            elif word < current.word:
                current = current.left

            # Search the right subtree if the word is greater
            else:
                current = current.right

        # Return None if the word does not exist
        return None

    # Write the BST in sorted order using inorder traversal
    def _write_inorder(self, node, file):

        # Stop when there is no node
        if node is None:
            return

        # First, write all words in the left subtree
        self._write_inorder(node.left, file)

        # Write the current word
        file.write(node.word + " -> ")

        # Write all line numbers associated with the word
        for line_number in node.line_numbers.get_lines():
            file.write(str(line_number) + " ")

        # Move to the next line in the output file
        file.write("\n")

        # Finally, write all words in the right subtree
        self._write_inorder(node.right, file)

    # Save the complete sorted index to a file
    def print_index(self, filename):

        # Open the output file in write mode
        with open(filename, "w", encoding="ascii") as file:

            # Start inorder traversal from the root
            self._write_inorder(self.root, file)
