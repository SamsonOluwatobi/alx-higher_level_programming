#!/usr/bin/python3

"""This module defines a Node class and a SinglyLinkedList class.

The Node class defines a node in a singly linked list with a data attribute and
a next_node attribute that points to the next node in the linked list.

The SinglyLinkedList class defines a singly linked list with a head attribute
that points to the first node in the linked list. It has a sorted_insert method
that inserts a new node with the given value in
the linked list in sorted order,
and a __str__ method that returns a string representation of the linked list.

Example:
    sll = SinglyLinkedList()
    sll.sorted_insert(3)
    sll.sorted_insert(1)
    sll.sorted_insert(2)
    print(sll)

Classes:
    Node: A class that defines a node in a singly linked list.
    SinglyLinkedList: A class that defines a singly linked list.
"""


class Node:
    """A class that defines a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node instance with the given data and next node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): The next node in the linked list.
            Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the data attribute.

        Returns:
            int: The data stored in the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """Setter for the data attribute.

        Args:
            value (int): The value to be stored in the node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Getter for the next_node attribute.

        Returns:
            Node: The next node in the linked list.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the next_node attribute.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If the value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self):
        """Initializes a new SinglyLinkedList instance with an empty head."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new node with the given value in the linked list
        in sorted order.

        Args:
            value (int): The value to be stored in the new node.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
