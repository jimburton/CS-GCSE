"""Huffman coding."""

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

    Each element of the output list is a tuple (n,c), where c
    is a character from text and n is its frequency.
    """
    pass

def build_queue(ftable) -> 'PriorityQueue':
    """Build the priority queue containing Huffman tree nodes."""
    pass

def merge(t1: 'HuffmanTree', t2: 'HuffmanTree') -> 'HuffmanTree':
    """Merge two Huffman trees.

    Make a new node whose frequency is the sum of the frequencies of the
    two nodes. Set the left and right children of the new node to be the
    two nodes, where the left-hand child has the lower frequency.
    """
    pass

def build_tree(pqueue: 'PriorityQueue') -> 'HuffmanTree':
    """Build the Huffman tree from the queue of nodes.

       While there is more than one node in the queue:
           . Take the first two nodes from the queue,
           . merge them,
           . put the resulting node back into the queue.

       Finally, return the last remaining node
    """
    pass
