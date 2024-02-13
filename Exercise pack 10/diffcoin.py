def count(x, coins):
    return helper(x, coins, len(coins))

def helper(x, coins, n):
    if x==0:
        return 1
    elif n==0 or x<0:
        return 0
    else:
        return helper(x, coins, n-1)+helper(x-coins[n-1], coins, n)


if __name__ == "__main__":
    print(count(5, [1])) # 1
    print(count(5, [1, 2])) # 3
    print(count(13, [1, 2, 5])) # 14
    print(count(42, [1, 5, 6, 17])) # 58
    print(count(99, [2, 4, 6])) # 0