#The function returns True if every leaf in a tree has the same depth

from collections import namedtuple

def check(node):
    return count_depth(node)

def count_depth(node):
    result = []
    depth_helper(node, 0, result)
    a = 0
    leaves = {}
    leaves[result[-1]] = 1
    for i in result[1:]:
        if result[a] >= i:
            leaves[result[a]] = 1
        a += 1

    if len(leaves) > 1:
        return False
    return True
                       
def depth_helper(node, depth, result):
    result.append(depth)
    for child in node.children:
        depth_helper(child, depth+1, result)




if __name__ == "__main__":
    Node = namedtuple("Node", ["children"], defaults=[[]])

    tree1 = Node([
                Node(),
                Node([Node([Node(), Node()])]),
                Node([Node(), Node()])
            ])

    tree2 = Node([Node([Node()]), Node([Node(), Node()])])

    tree3 = Node(children=[Node(children=[]), Node(children=[Node(children=[])])])

    print(check(tree1)) # False
    print(check(tree2)) # True
    print(check(tree3)) #False
