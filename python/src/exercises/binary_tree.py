class Tree:
    """A class to represent binary trees."""

    def __init__(self, label, left=None, right=None):
        """Constructor for Tree objects."""
        self.label = label
        self.left = left
        self.right = right

    def insert(self, label):
        """Insert a new node to the tree."""
        if label == self.label:
            return # we don't want any duplicates
        node = Tree(label)
        if label < self.label:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(label)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(label)

    def search(self, target) -> bool:
        """Search this tree for a target value."""
        pass
    
    def count_nodes(self):
        """Count the number of nodes in this tree."""
        pass

    def min(self):
        """Find the smallest label in the tree."""
        pass

def print_tree(node, level=0):
    if node != None:
        print_tree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.label))
        print_tree(node.right, level + 1)
