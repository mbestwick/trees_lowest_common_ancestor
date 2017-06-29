"""
You are given pointer to the root of the binary search tree and two values v1
and v2. You need to return the lowest common ancestor (LCA) of v1 and v2 in the
binary search tree. You only need to complete the function.

"""


class Node(object):
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def lca(root, v1, v2):
    if root.data < v1 and root.data < v2:
        return lca(root.right, v1, v2)
    if root.data > v1 and root.data > v2:
        return lca(root.left, v1, v2)
    else:
        return root
