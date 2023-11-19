def solve(t):
    moves = 0

    if len(t) > 1:
        half = len(t)//2

        left = t[:half]
        right = t[half:]

        maxl = half
        minr = half+1

        lefts = {}
        rights = {}

        idx = 0
        for i in left:
            if i > maxl:
                lefts[i] = idx
            idx += 1

        idx = 0
        for i in right:
            if i < minr:
                rights[i] = idx
            idx += 1

        moves = counter(lefts, rights, len(left))
    return moves


def counter(lefts, rights, n):

    moves = 0

    for key in lefts:
        moves += n-lefts[key]
    moves += len(lefts)

    for key in rights:
        moves += rights[key]-1

    return moves


if __name__ == "__main__":
    print(solve([2, 1, 4, 3])) # 0
    print(solve([5, 3, 4, 1, 6, 2])) # 6
    print(solve([6, 5, 4, 3, 2, 1])) # 9
    print(solve([10, 1, 9, 2, 8, 3, 7, 4, 6, 5])) # 15