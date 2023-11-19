def solve(t, x):
    t.sort()
    sum = 0
    i = 0
    for pack in t:
        i += 1
        sum += pack
        if sum > x:
            return i-1
    return i

if __name__ == "__main__":
    print(solve([1, 1, 1, 1], 2)) # 2
    print(solve([2, 5, 3, 2, 8, 7], 10)) # 3
    print(solve([2, 3, 4, 5], 1)) # 0
    print(solve([2, 3, 4, 5], 10**9)) # 4
    print(solve([10**9, 1, 10**9], 10**6)) # 1