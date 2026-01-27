"""Huffman coding.

Some functions left as exercises.
"""
from huffman_tree import HuffmanTree
from pqueue import PriorityQueue

def frequency_table(text: str) -> dict:
    """Construct the frequency table for the input text.

    Count the occurences of each character in the input text.

    1. Make a new, empty dictionary.
    2. For each character in the input text, check whether it is already
    a key in the dictionary. If it is not, make it into a key with the
    value 0. If it is already in the dictionary, add 1 to its value.
    3. Return the dict.
    """
    frequency = {}
    for char in text:
        if not char in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1
    return frequency
        

def build_queue(ftable: dict) -> 'PriorityQueue':
    """Build the priority queue containing Huffman tree nodes.

     
    
    1. Make a new PriorityQueue.
    2. for each key in the frequency table, create a new HuffmanTree
    object with the character and frequency from the frequency table and
    enqueue it.
    3. Finally, return the queue.
    """
    pqueue = PriorityQueue()
    for char,frequency in ftable.items():
         huffman = HuffmanTree(frequency,char)
         pqueue.enqueue(huffman,frequency)
    return pqueue

def merge(t1: 'HuffmanTree', t2: 'HuffmanTree') -> 'HuffmanTree':
    """Merge two Huffman trees.
    
    1. Make a new node whose frequency is the sum of the frequencies of the
    two nodes.
    2. Set the left and right children of the new node to be the
    two nodes, where the left-hand child has the lower frequency.
    3. Return the new node.
    """
    left = t1 if t1.frequency < t2.frequency else t2
    right = t1 if left == t2 else t2
    node = HuffmanTree(t1.frequency + t2.frequency, left=left, right=right)
    return node

def build_tree(pqueue: 'PriorityQueue') -> 'HuffmanTree':
    """Build the Huffman tree from the queue of nodes.

    TODO
    
    1. While there is more than one node in the queue:
        a) Take the first two nodes from the queue,
        b) merge the nodes into a new node,
        c) put the new node back into the queue.
    2. Return the last remaining node
    """
    while pqueue.length() >= 2:
        t1 = pqueue.dequeue()
        t2 = pqueue.dequeue()
        node = merge(t1, t2)
        pqueue.enqueue(node,node.frequency)
    final_node = pqueue.dequeue()
    return final_node
    

def build_codes(tree: 'HuffmanTree') -> dict:
    """Transform a Huffman tree into a dict.

    In the dict the keys are characters and the values are their Huffman codes.
    """
    return collect_codes(tree, path=[])

def collect_codes(tree: 'HuffmanTree', path: list) -> dict:
    """Helper method for tree_to_dict.

    Traverses the tree to collect all codes.
    """
    if not tree.char is None:    # We are at a leaf.
        return {tree.char: path}
    else:                        # We are in a branch.
        # Copy the path before modifying it.
        left_path = path.copy()
        left_path.append(0b0)
        right_path = path.copy()
        right_path.append(0b1)
        left = {} if tree.left is None else collect_codes(tree.left, left_path)
        right = {} if tree.right is None else collect_codes(tree.right, right_path)
        return {**left, **right}

def encode(input: str) -> tuple:
    """Create the Huffman coding for an input string.
    
    Returns the encoded data and the dict for decoding.
    The dict is a map from characters to codes, where each code is a list
    of zeros and ones.
    
    TODO

    1. First, create the frequency table for input.
    2. Build the priority queue containing leaf nodes.
    3. Build the complete Huffman tree.
    4. Collect the codes from the tree.
    5. Map the codes onto the input and return the encoded version.
    
    """
    frequency = frequency_table(input)
    queue = build_queue(frequency)
    tree = build_tree(queue)
    codes = build_codes(tree)
    result = []
    for char in input:
        result += codes[char]
    return (result, codes)
    

def tree_from_dict(code: dict) -> 'HuffmanTree':
    """Rebuild the Huffman tree from the dictionary of codes.

    This tree is useful only for its structure, so frequencies are ignored."""
    root = HuffmanTree(0)
    for (char,path) in code.items():
        node = root
        for ix,step in enumerate(path):
            next_node = HuffmanTree(0) if ix < len(path) - 1 else HuffmanTree(0, char)
            if step == 0b0:
                if node.left == None:
                    node.left = next_node
                node = node.left
            else:
                if node.right == None:
                    node.right = next_node
                node = node.right
    return root
    
def decode(enc: list, coding: dict) -> str:
    """Decode some Huffman code.

    `enc` is the encoded input and dict contains the code.

    TODO
    
    1. Build the Huffman tree from the dict.
    2. Create an empty string to hold the result.
    3. For each code in `enc`, add the corresponding char to the result.
    4. Return the result.
    """
    tree = tree_from_dict(coding)
    result = ""
    node = tree
    for bit in enc:
        if node.char is not None: # this is a leaf node
            result += node.char
            node = tree
        if bit == 1:
            node = node.right
        else:
            node = node.left
    return result

def test_huffman_codec():
    """Test that we can encode and decode with the Huffman coding."""
    s = """Decode some Huffman coded input.

    `enc` is the encoded input and dict contains the code.

    1. Build the Huffman tree from the dict.
    2. Create an empty string to hold the result.
    3. For each code in `enc`, add the corresponding char to the result.
    4. Return the result.
    """
    (enc, code) = encode(s)
    print(s)
    dec = f"{decode(enc, code)}"
    print(dec)
    print(f"{len(s)=}")
    print(f"{len(dec)=}")
    assert(s == dec)
        
def test_frequency_table():
    table = frequency_table("hello world")
    assert(table["l"] == 3)
    assert( not "i" in table )
    print (" everything is working in the frequency table")
