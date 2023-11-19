#You are given a list with numbers 1...n in some order. The goal is to 
#sort a list with two commands: swap (swap first two adajcent numbers in a list)
#and move (move the first number in a list to the end).
#The goal is to create an algorithm with max of n^3 commands.
#The function returns a list of commands.

def solve(t):
    n = len(t)
    order = t.copy()
    target = list(range(1,n+1))
    result = []
    while order != target:
        if order[0] > order[1] and order[1] != 1:
            result.append("SWAP")
            order = [order[1]] + [order[0]] + order[2:]
        else:
            result.append("MOVE")
            order = order[1:] + [order[0]]
    return result