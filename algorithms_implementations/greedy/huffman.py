from queue import PriorityQueue


class Word:

    def __init__(self, number, val=None):
        self.val = val
        self.number = number
        self.add = None
        self.leftChild = None
        self.rightChild = None
        self.finalAddres = None

    def set_left_child(self, child):
        child.add = 0
        child.parent = self
        self.leftChild = child

    def set_right_child(self, child):
        child.add = 1
        child.parent = self
        self.rightChild = child

    def go_to_child(self, list_of_sizes, addr):
        printed = False
        if self.add is not None:
            addr = addr + str(self.add)
            kr = (self.val, len(addr))
            list_of_sizes.append(kr)

        if self.leftChild is not None:
            var = self.leftChild.go_to_child(list_of_sizes, addr)
        else:
            print(self.val + " : " + addr)
            printed = True
        if self.rightChild is not None:
            var = self.rightChild.go_to_child(list_of_sizes, addr)
        else:
            if not printed:
                print(self.val + " : " + addr)

    def print_parent_add(self):
        print(self.add)
        if self.parent is not None:
            self.print_parent_add()


def huffman(S, F):
    queue = PriorityQueue()

    for i in range(len(S)):
        queue.put((F[i], Word(F[i], S[i])))

    while queue.qsize() > 1:
        x1, x2 = queue.get()
        y1, y2 = queue.get()
        word = Word(x1 + y1)
        word.set_left_child(x2)
        word.set_right_child(y2)
        queue.put((word.number, word))

    x1, x2 = queue.get()

    list_of_sizes = []
    x2.go_to_child(list_of_sizes, addr="", )
    sum = 0
    for i in list_of_sizes:
        x, y = i
        if x is not None:
            for j in range(len(S)):
                if x == S[j]:
                    ingredient = y * F[j]
                    sum += ingredient

    print("Długość napisu to:", sum)
