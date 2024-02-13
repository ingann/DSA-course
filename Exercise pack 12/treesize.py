
class TreeSet:
    def __init__(self):
        self.root = None
        self.len = 0

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            self.len += 1
            return

        node = self.root
        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    self.len += 1
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    self.len += 1
                    return
                node = node.right

    def __len__(self):
        return self.len

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == "__main__":
    s = TreeSet()
    print(len(s)) # 0
    s.add(1)
    print(len(s)) # 1
    s.add(2)
    print(len(s)) # 2
    s.add(3)
    print(len(s)) # 3
    s.add(2)
    print(len(s)) # 3