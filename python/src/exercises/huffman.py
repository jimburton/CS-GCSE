"""Huffman coding.

Some functions left as exercises.
"""

class HuffmanTree:
    """Class for nodes in a Huffman tree."""

    def __init__(self, frequency, char=None, left=None, right=None):
        """Constructor for Huffman trees."""
        self.frequency = frequency
        self.char = char
        self.left = left
        self.right = right

class PriorityQueue:
    """Class for priority queues."""

    def __init__(self):
        """Constructor for priority queues."""
        self._data = []

    def enqueue(self, item, priority):
        """Insert a new item with the given priority into the queue."""
        index = 0
        found = False
        for (i,(element, p)) in enumerate(self._data):
            if p >= priority:
                index = i
                found = True
                break
        if not found:
            index = len(self._data)
        self._data.insert(index, (item, priority))

    def dequeue(self):
        """Remove the first item from the queue."""
        if len(self._data) > 0:
            (item,_) = self._data[0]
            self._data = self._data[1:]
            return item

def frequency_table(text: str) -> list:
    """Construct the frequency table for the input text.

    Count the occurences of each character in the input text.

    1. Make a new, empty dictionary.
    2. For each character in the input text, check whether it is already
    a key in the dictionary. If it is not, make it into a key with the
    value 0. If it is already in the dictionary, add 1 to its value.
    3. Create an empty list to hold the result.
    4. Loop through the keys and values of the dictionary and add each pair
    to the list as a tuple, (n,c), where n is the count and c is the character.
    """
    pass

def build_queue(ftable) -> 'PriorityQueue':
    """Build the priority queue containing Huffman tree nodes.

    TODO
    
    1. Make a new PriorityQueue.
    2. for each item in the frequency table, create a new HuffmanTree
    object with the character and frequency from the frequency table and
    enqueue it.
    3. Finally, return the queue.
    """
    pass

def merge(t1: 'HuffmanTree', t2: 'HuffmanTree') -> 'HuffmanTree':
    """Merge two Huffman trees.

    TODO
    
    1. Make a new node whose frequency is the sum of the frequencies of the
    two nodes.
    2. Set the left and right children of the new node to be the
    two nodes, where the left-hand child has the lower frequency.
    3. Return the new node.
    """
    pass

def build_tree(pqueue: 'PriorityQueue') -> 'HuffmanTree':
    """Build the Huffman tree from the queue of nodes.

    TODO
    
    1. While there is more than one node in the queue:
        a) Take the first two nodes from the queue,
        b) merge the nodes into a new node,
        c) put the new node back into the queue.
    2. Return the last remaining node
    """
    pass

def tree_to_dict(tree: 'HuffmanTree') -> dict:
    """Transform a Huffman tree into a dict.

    In the dict the keys are characters and the values are their Huffman codes.
    """
    return collect_codes(tree, code=[])

def collect_codes(tree: 'HuffmanTree', code) -> dict:
    """Helper method for tree_to_dict.

    Traverses the tree to collect all codes.
    """
    if not tree.char is None:    # We are at a leaf.
        return {tree.char: path}
    else:                        # We are in a branch.
        # Copy the path before modifying it.
        left_path = path.copy()
        left_path.append(b0)
        right_path = path.copy()
        right_path.append(b1)
        left = {} if tree.left is None else collect_codes(tree.left, left_path)
        right = {} if tree.right is None else collect_codes(tree.right, right_path)
        return {**left, **right}

def encode(input: str) -> list:
    """Create the Huffman coding for an input string.
    
    The dict is a map from characters to codes, where each code is a list
    of zeros and ones.
    
    TODO

    1. First, create the frequency table for input.
    2. Build the priority queue containing leaf nodes.
    3. Build the complete Huffman tree.
    4. Collect the codes from the tree.
    5. Map the codes onto the input and return the encoded version.
    
    """
    pass
