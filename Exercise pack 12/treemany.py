
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, value, node=None):
        if node == None:
            if self.root == None:
                self.root = Node(value)
            else:
                self.add(value, self.root)
            return

        if node.value == value:
            node.count += 1
            return

        if node.value > value:
            if node.left == None:
                node.left = Node(value)
            else:
                self.add(value, node.left)

        if node.value < value:
            if node.right == None:
                node.right = Node(value)
            else:
                self.add(value, node.right)

    def __contains__(self, value, node=None):
        if node == None:
            if self.root == None:
                return False
            return self.__contains__(value, self.root)

        if node.value == value:
            return True

        if node.value > value:
            if node.left == None:
                return False
            return self.__contains__(value, node.left)
        else:
            if node.right == None:
                return False
            return self.__contains__(value, node.right)

    def __repr__(self):
        items = []
        self.traverse(self.root, items)
        return str(items)

    def traverse(self, node, items):
        if node == None:
            return
        self.traverse(node.left, items)
        for i in range(node.count):
            items.append(node.value)
        self.traverse(node.right, items)

    def count(self, value):
        if not self.__contains__(value):
            return 0

        node = self.root
        while node.value != value:
            if value < node.value:
                node = node.left
            else:
                node = node.right

        return node.count

if __name__ == "__main__":
    s = TreeSet()
    s.add(4)
    s.add(1)
    s.add(2)
    s.add(1)
    print(s) # [1, 1, 2, 4]
    print(1 in s) # True
    print(2 in s) # True
    print(3 in s) # False
    print(4 in s) # True
    print(s.count(1)) # 2
    print(s.count(2)) # 1
    print(s.count(3)) # 0
    print(s.count(4)) # 1