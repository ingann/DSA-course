#I utilized this solution in my code: https://www.geeksforgeeks.org/find-the-maximum-depth-or-height-of-a-tree/
class TreeSet:
    def __init__(self):
        self.root = None
        self.len = 0
        self.h = -1


    def add(self, value):

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



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == "__main__":
    s = TreeSet()
    print(s.height()) # -1
    s.add(2)
    print(s.height()) # 0
    s.add(1)
    print(s.height()) # 1
    s.add(3)
    print(s.height()) # 1
    s.add(4)
    print(s.height()) # 2