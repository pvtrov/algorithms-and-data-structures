from egzP4btesty import runtests


class Node:
    def __init__(self, key, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.x = None


def find_prev(root):
    if root.right is not None:
        root = root.right
        while root.left is not None:
            root = root.left
        return root.key
    else:
        p_root = root.parent
        while p_root is not None:
            if root != p_root.right:
                return p_root.key
            root = p_root
            p_root = p_root.parent


def find_next(root):
    if root.left is not None:
        root = root.left
        while root.right is not None:
            root = root.right
        return root.key
    else:
        l_root = root.parent
        while l_root is not None:
            if root != l_root.left:
                return l_root.key
            root = l_root
            l_root = l_root.parent


def sol(root, T):
    sum_ = 0
    for temp_root in T:
        predecessor = find_prev(temp_root)
        consequent = find_next(temp_root)
        almost_av = predecessor + consequent
        if almost_av == temp_root.key * 2:
            sum_ += temp_root.key

    return sum_

runtests(sol, all_tests = True)

# w11 = Node(11, None)
# w5 = Node(5, w11)
# w11.left = w5
# w15 = Node(15, w11)
# w11.right = w15
# w3 = Node(3, w5)
# w5.left = w3
# w8 = Node(8, w5)
# w5.right = w8
# w12 = Node(12, w15)
# w15.left = w12
# w7 = Node(7, w8)
# w8.left = w7
# w10 = Node(10, w8)
# w8.right = w10
# T = [ w5, w7, w8, w10, w11, w12 ]
# print(sol(w11, T))
