class LineNode:
    def __init__(self, line_number):
        self.line_number = line_number
        self.next = None


class LineList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, line_number):
        # Do not store the same line number more than once
        if self.tail is not None and self.tail.line_number == line_number:
            return

        new_node = LineNode(line_number)

        # If the list is empty, the new node becomes both head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # Otherwise, add the node at the end of the queue
        else:
            self.tail.next = new_node
            self.tail = new_node

    def get_lines(self):
        # Convert the linked list into a normal Python list
        lines = []

        current = self.head

        while current is not None:
            lines.append(current.line_number)
            current = current.next

        return lines