##The function returns the max amount of children in the node of a tree

from collections import namedtuple

def count(node):
    result = len(node.children)
    for child in node.children:
        biggest = count(child)
        if biggest > result:
            result = biggest
    return result
        

if __name__ == "__main__":
    Node = namedtuple("Node", ["children"], defaults=[[]])

    tree1 = Node([
                Node(),
                Node([Node([Node(), Node()])]),
                Node([Node(), Node()])
            ])

    tree2 = Node([Node([Node(), Node()])])

    tree3 = Node(children=[Node(children=[]), Node(children=[])])

    tree4 = Node(children=[Node(children=[Node(children=[Node(children=[])])])])


    print(count(tree1)) # 3
    print(count(tree2)) # 2
    print(count(tree3)) #2
    print(count(tree4)) #1
