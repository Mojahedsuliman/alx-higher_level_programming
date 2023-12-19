#!/usr/bin/python3

"""Defines classes for singly linked list."""

class Node:
    """Represents the node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        
        Args:
        data (int): The data of the new Node.
        next_node (Node): The next node of the new Node.
        """

        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """Get or set the data of the node."""
            return self.__data
        
        @data.setter
        def data(self, value):
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            """Get or set the next node of the node."""
            return self.__next_node
        
        @next_node.setter
        def next_node(self, value):
            if not isinstance(value, Node) and value is not None:
                raise TypeError("next_node must be a Node object")
            self.__next_node = value

    class singly_linked_list:
            """Represents a singly linked list."""

        def __init__(self):
            """Initialize a new SinglyLinkedList."""
            self.__head = None
        
        def sorted_insert(self, value):
            """Insert a new Node to the SinglyLinkedList"""
            new = Node(value)
            if self.__head is None:
                 new.next_node = None
                 self.__head = new
            elif value < (self.__head.data):
                 new.next_node = self.__head
                 self.__head = new
            else:
                 temp = self.__head
                 while (temp.next_node is not None and
                     temp.next_node.data < value):
                     temp = temp.next_node
                     new.next_node = temp.next_node
                     temp.next_node = new
        def __str__(self):
             """Define the print() representation of a SinglyLinkedList."""
              values = []
              temp = self.__head
              while temp is not None:
                     values.append(str(temp.data))
                     temp = temp.next_node
                     return ('\n'.join(values))
