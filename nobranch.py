#The goal is to find out is a tree has no branches (every node has at most one child)
#The function returns if a tree has branches (False) or not (True)

from collections import namedtuple

def check(node):
    branch = True
    if len(node.children) > 1:
        return False
    for child in node.children:
        branch = check(child)
    return branch


if __name__ == "__main__":
    Node = namedtuple("Node", ["children"], defaults=[[]])

    tree1 = Node([
                Node(),
                Node([Node([Node(), Node()])]),
                Node([Node(), Node()])
            ])

    tree2 = Node([Node([Node([Node()])])])

    print(check(tree1)) # False
    print(check(tree2)) # True
