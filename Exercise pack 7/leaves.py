#The function returns a count of leaves in a tree

from collections import namedtuple

def count(node):
    result = 0
    if node.children == []:
        result += 1
    for child in node.children:
        result += count(child)

    return result

if __name__ == "__main__":
    Node = namedtuple("Node", ["children"], defaults=[[]])

    tree = Node([
               Node(),
               Node([Node([Node(), Node()])]),
               Node([Node(), Node()])
           ])

    print(count(tree)) # 5

    tree2 = Node(children=[Node(children=[Node(children=[])])])
    print(count(tree2)) #1

    tree3 = Node(children=[])
    print(count(tree3))#1
