class HuffmanTree:
    """Class for nodes in a Huffman tree."""

    def __init__(self, frequency: int,
                 char: str=None,
                 left: 'HuffmanTree'=None,
                 right: 'HuffmanTree' =None):
        """Constructor for Huffman trees."""
        self.frequency = frequency
        self.char = char
        self.left = left
        self.right = right

    def __str__(self):
        """String representation of the tree."""
        return tree_to_string(self)

    def __repr__(self):
        """String representation for debugging."""
        return self.__str__()

def tree_to_string(node, level=0):
    """Helper method for printing tree instances."""
    result = ""
    if node != None:
        result += tree_to_string(node.left, level + 1) + "\n"
        result += f"{' ' * 4 * level} -> {str(node.char)} {node.frequency} \n"
        result += tree_to_string(node.right, level + 1) + "\n"
    return result
