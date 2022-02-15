
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def find(root, key):
        while root is not None:
            if root.key == key:
                return root
            elif key < root.key:
                root = root.left
            else:
                root = root.right
        return None
