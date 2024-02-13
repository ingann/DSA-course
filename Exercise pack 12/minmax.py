class TreeSet:
    def __init__(self):
        self.root = None
        self.len = 0
        self.h = -1
        self.minimum = -1
        self.maximum = -1

    def add(self, value):

        if value < self.minimum or self.minimum == -1:
            self.minimum = value
        if value > self.maximum or self.maximum == -1:
            self.maximum = value
        if not self.root:
            self.root = Node(value)
            self.len += 1
            self.h += 1
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


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



if __name__ == "__main__":
    s = TreeSet()
    print(s.min()) # None
    print(s.max()) # None
    s.add(1)
    s.add(2)
    s.add(3)
    print(s.min()) # 1
    print(s.max()) # 3