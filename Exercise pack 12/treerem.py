class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class TreeSet:
    def __init__(self):
        self.root = None
        self.len = 0

    def __repr__(self):
        items = []
        self.traverse(self.root, items)
        return str(items)

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
    
    def height(self, node=None):
        if not node:
            if not self.root:
                return -1
            return self.height(self.root)

        result = 0
        if node.left:
            result = max(result, self.height(node.left) + 1)
        if node.right:
            result = max(result, self.height(node.right) + 1)
        return result
            
    def min(self):
        if self.root == None:
            return None

        node = self.root
        while node.left != None:
            node = node.left

        return node.value

    def max(self):
        if self.root == None:
            return None

        node = self.root
        while node.right != None:
            node = node.right

        return node.value
    
    def prev(self, x):
        if self.root == None:
            return None
 
        node = self.root
        result = None
 
        while node:
            if node.value < x:
                if not result or result < node.value:
                    result = node.value
                node = node.right
            else:
                node = node.left
 
        return result
 
    def next(self, x):
        if self.root == None:
            return None
 
        node = self.root
        result = None
 
        while node:
            if node.value > x:
                if not result or result > node.value:
                    result = node.value
                node = node.left
            else:
                node = node.right
 
        return result
    
    def remove(self, x):

        if not self.__contains__(x):
            return

        node, parent = self.find_ref(x)

        if node.left and node.right:
            ref = self.find_ref(self.next(x))
            node.value = ref[0].value
            node, parent = ref

        child = None
        if node.left:
            child = node.left
        if node.right:
            child = node.right

        if parent:
            if parent.left == node:
                parent.left = child
            else:
                parent.right = child
        else:
            self.root = child

    def find_ref(self, x):
        parent = None
        node = self.root

        while node.value != x:
            parent = node
            if node.value > x:
                node = node.left
            else:
                node = node.right

        return (node, parent)

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
    
    def traverse(self, node, items):
        if not node:
            return
        self.traverse(node.left, items)
        items.append(node.value)
        self.traverse(node.right, items)


if __name__ == "__main__":
    s = TreeSet()
    s.add(2)
    s.add(1)
    s.add(3)
    s.add(4)
    print(s) # [1, 2, 3, 4]
    s.remove(3)
    print(s) # [1, 2, 4]
    s.remove(2)
    print(s) # [1, 4]
    s.remove(1)
    print(s) # [4]
    s.remove(1)
    print(s) # [4]