class TreeSet:
    def __init__(self):
        self.root = None
        self.len = 0
        self.h = -1
        self.minimum = -1
        self.maximum = -1
        self.nodes = {}

    def add(self, value):

        self.nodes[value] = 1

        if value < self.minimum or self.minimum == -1:
            self.minimum = value
        if value > self.maximum or self.maximum == -1:
            self.maximum = value
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
    
    def height(self):
        self.h = self.depth(self.root)-1
        return self.h

    def depth(self, node):
        if node is None:
            return 0
    
        else:
    
            # Compute the depth of each subtree
            leftD = self.depth(node.left)
            rightD = self.depth(node.right)
    
            # Use the larger one
            if (leftD > rightD):
                return leftD+1
            else:
                return rightD+1
            
    def min(self):
        if self.len == 0:
            return None
        return self.minimum

    def max(self):
        if self.len == 0:
            return None
        return self.maximum
    
    def prev(self, x):
        self.nodes = dict(sorted(self.nodes.items()))
        smallest = x
        for node in self.nodes:
            if node < smallest:
                smallest = node
            elif smallest<node<x:
                smallest = node
        if smallest == x:
            return None
        return smallest

    def next(self, x):
        self.nodes = dict(sorted(self.nodes.items()))
        for node in self.nodes:
            if node > x:
                return node
        return None
    
    def __contains__(self, value):
        if not self.root:
            return False

        node = self.root
        while node:
            if node.value == value:
                return True
            if node.value > value:
                node = node.left
            else:
                node = node.right

        return False

        

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == "__main__":
    s = TreeSet()
    s.add(2)
    s.add(5)
    print(s.prev(5)) # 2
    print(s.prev(2)) # None
    print(s.next(1)) # 2
    print(s.next(2)) # 5
    print(s.next(5)) # None
    print()

    s = TreeSet()
    s.add(10)
    print(s.prev(9))
    print(s.next(6))
    s.add(10)
    print(s.prev(10))
    print(s.next(3))
    s.add(6)
    print(s.prev(7))
    print(s.next(6))
    s.add(5)
    print(s.prev(7))
    print(s.next(4))
    s.add(6)
    print(s.prev(2))
    print(s.next(7))
    s.add(7)
    print(s.prev(2))
    print(s.next(9))
    s.add(6)
    print(s.prev(7))
    print(s.next(7))
    s.add(5)
    print(s.prev(1))
    print(s.next(6))
    s.add(10)
    print(s.prev(2))
    print(s.next(8))
    s.add(4)
    print(s.prev(3))
    print(s.next(6))