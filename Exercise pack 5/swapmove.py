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