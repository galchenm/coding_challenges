"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

def serialize(root):
    """Encodes a tree to a single string."""
    def helper(node):
        if not node:
            return 'None,'
        return f'{str(node.val)},{helper(node.left)}{helper(node.right)}'
    
    return helper(root)

def deserialize(data):
    """Decodes your encoded data to tree."""
    def helper(nodes):
        val = next(nodes)
        if val == 'None':
            return None
        node = Node(val)
        node.left = helper(nodes)
        node.right = helper(nodes)
        return node
    
    nodes = iter(data.split(','))
    return helper(nodes)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    # Example usage 
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    serialized = serialize(node)
    print(f"Serialized: {serialized}")
    deserialized = deserialize(serialized)
    print(f"Deserialized left.left value: {deserialized.left.left.val if deserialized.left and deserialized.left.left else 'None'}")
    # Test case to check if the deserialized tree matches the original tree
    assert deserialized.left.left.val == 'left.left'
    # Additional test cases can be added here to validate the functionality
    #
    # Example of a tree structure to test serialization and deserialization
    #         root
    #        /    \
    #      left   right
    #      /  \
    # left.left  None       
    # The serialized string should represent the structure of the tree
    # and the deserialized tree should match the original tree structure.
    # The assert statement checks if the deserialized tree's left.left value is as expected.
    