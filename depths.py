#The function returns the sum of the nodes' depths in a tree

from collections import namedtuple
 
def count(node):
    result = len(node.children)
    for child in node.children:
        print(count(child))
    return result
if __name__ == "__main__":
    Node = namedtuple("Node", ["children"], defaults=[[]])

    tree = Node([
               Node(),
               Node([Node([Node(), Node()])]),
               Node([Node(), Node()])
           ])

    print(count(tree)) # 15
