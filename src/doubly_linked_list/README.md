
# Doubly Linked List Implementation in Python

## Overview

This project implements a **Doubly Linked List (DLL)** in Python, which supports efficient insertion and deletion of elements from both the front and the back of the list. Each node contains a reference to both its previous and next nodes, allowing traversal in both directions.

The main files in this implementation are:

- **`node.py`**: Defines the `Node` class, representing an individual node in the list.
- **`doubly_linked_list.py`**: Implements the `DoublyLinkedList` class, providing various methods for managing the list.
- **`main.py`**: Contains example usage of the `DoublyLinkedList` class.

## Features

- **Insert at Front**: Add a new element to the front of the list.
- **Insert at Back**: Add a new element to the end of the list.
- **Insert at Position**: Add a new element at a specified position in the list.
- **Delete from Front**: Remove the element at the front of the list.
- **Delete from Back**: Remove the element at the back of the list.
- **Delete from Position**: Remove an element from a specified position in the list.
- **Check Head and Tail**: Retrieve the data from the head or tail of the list.
- **Traverse**: Print the current state of the list.

## Class Descriptions

### `Node` (in `node.py`)
The `Node` class represents each node in the doubly linked list. It contains:
- `data`: The value stored in the node.
- `nxt`: A reference to the next node in the list.
- `prev`: A reference to the previous node in the list.

#### Methods:
- `get_data()`: Returns the data stored in the node.
- `set_data(new_value)`: Sets new data for the node.
- `get_next()`: Returns the next node.
- `get_previous()`: Returns the previous node.

### `DoublyLinkedList` (in `doubly_linked_list.py`)
The `DoublyLinkedList` class manages the list and provides methods for insertion, deletion, and traversal.

#### Methods:
- `insert_at_front(data)`: Inserts a new node at the front of the list.
- `insert_at_back(data)`: Inserts a new node at the back of the list.
- `insert_at(data, pos)`: Inserts a new node at the specified position.
- `delete_at_front()`: Removes the front node.
- `delete_at_back()`: Removes the back node.
- `delete_at(pos)`: Removes a node at the specified position.
- `check_head()`: Returns the data from the head of the list.
- `check_tail()`: Returns the data from the tail of the list.
- `__str__()`: Provides a string representation of the list.

## Example Usage

Here's an example of how you can use the `DoublyLinkedList` class in your code:

```python
from doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList(10)

dll.insert_at_front(1)
print(dll)

dll.insert_at_front(2)
print(dll)

dll.insert_at_back(5)
print(dll)

dll.insert_at(10, 3)
print(dll)

dll.delete_at_front()
print(dll)

dll.delete_at_back()
print(dll)
```

## Installation and Setup

To use this implementation, clone the repository and ensure that the Python files are in the same directory. Import the `DoublyLinkedList` class in your scripts and start using the available methods.

### Requirements:
- Python 3.x
- Basic knowledge of data structures

## Logging

Logging is enabled at the `INFO` level. You can modify the logging level in the `doubly_linked_list.py` file to display more detailed logs (such as `DEBUG`) or suppress unnecessary information (by setting to `ERROR` or `WARNING`).

## Contributing

Feel free to contribute to this project by submitting a pull request or opening an issue.

## License

This project is licensed under the MIT License.
