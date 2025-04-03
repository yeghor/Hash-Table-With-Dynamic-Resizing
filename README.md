Here is a README file in English for the `hash_map.py` file in your repository:

```Python
# Hash Table With Dynamic Resizing

This project implements a hash table with dynamic resizing in Python. The implementation allows efficient data management and optimized memory usage.

## File: `hash_map.py`

The file `hash_map.py` contains the implementation of the hash table. Below are the key components and methods:

### Classes and Methods

- **Node**: Represents a single node in the hash table.
  - `__init__(self, key, value)`: Initializes a node with a given key and value.

- **HashMap**: Main class representing the hash table.
  - `__init__(self, start_capacity=10, expand_factor=2)`: Initializes the hash table with a specified initial capacity and expansion factor.
  - `__iter__(self)`: Returns an iterator for the hash table.
  - `__str__(self)`: Returns a string representation of the hash table.
  - `get(self, key)`: Retrieves the value associated with the given key.
  - `delete_by_key(self, key) -> bool`: Deletes the key-value pair from the hash table.
  - `add(self, key, value)`: Adds a key-value pair to the hash table.
  - `__capacity_logic(self)`: Checks and manages the capacity of the hash table.
  - `__check_capacity(self) -> bool`: Checks if the current load factor requires resizing.
  - `__add_internal(node: Node, actual_array)`: Adds a node to the specified array.
  - `__increase_capacity(self)`: Increases the capacity of the hash table by the expansion factor.

### Example Usage

```python
from hash_map import HashMap

# Create a new hash table
hash_map = HashMap()

# Add values
hash_map.add("key1", "value1")
hash_map.add("key2", "value2")

# Retrieve values
print(hash_map.get("key1"))  # Output: value1

# Delete a value
hash_map.delete_by_key("key2")

# Check the size
print(len(hash_map))  # Output: 1
```

### Description of Methods

- **`get(self, key)`**: Uses the hash function to find the index of the key and iterates through the linked list at that index to find and return the value.
- **`delete_by_key(self, key) -> bool`**: Finds the key using the hash function and removes the corresponding node from the linked list.
- **`add(self, key, value)`**: Inserts a new key-value pair into the hash table, resizing the table if necessary.
- **`__capacity_logic(self)`**: Checks if the hash table needs to be resized and resizes it if necessary.
- **`__check_capacity(self) -> bool`**: Checks if the load factor exceeds the threshold (0.75) to decide if resizing is needed.
- **`__add_internal(node: Node, actual_array)`**: Adds a node to the specified array, handling collisions by chaining.
- **`__increase_capacity(self)`**: Doubles the size of the hash table and rehashes all existing key-value pairs.

This README file provides a comprehensive overview of the structure and functionality of `hash_map.py`, including example usage and a description of the methods. You can customize and expand it based on the specific details and requirements of your project.
