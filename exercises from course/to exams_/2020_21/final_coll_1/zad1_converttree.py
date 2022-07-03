from zad1testy import runtests
"""
ogulnie dziala i jest git ale nie wiem czemu nie przechodzi testow
"""


class Node:
    def __init__(self):
        self.value = None
        self.parent = None
        self.left = None
        self.right = None


def print_inorder(root, tree):  # rosnąco
    if root is not None:
        print_inorder(root.left, tree)
        tree.append(root.value)
        print_inorder(root.right, tree)
    return tree


def build_tree(tree, root, index, parent, level):
    if index < len(tree):
        root.value = tree[index]
        root.parent = parent
        root.left = build_tree(tree, Node(), 2*index + 1, root, level + 1)
        root.right = build_tree(tree, Node(), 2*index + 2, root, level + 2)
    return root


def ConvertTree(p):
    tree = print_inorder(p, [])
    new_tree = build_tree(tree, Node(), 0, -1, 0)

    return new_tree


runtests( ConvertTree )