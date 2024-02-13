import itertools
def count(n, x):
    items = list(range(1, n + 1))
    count = 0

    for order in itertools.permutations(items):
        if valid_order(order) and order[0] == x:
            count += 1

    return count

def valid_order(order):
    sums = {}
    for i in range(len(order) - 1):
        if abs(order[i] + order[i + 1]) in sums:
            return False
        sums[abs(order[i]+order[i+1])] = 1
    return True


if __name__ == "__main__":
    print(count(1, 1)) # 1
    print(count(4, 2)) # 4
    print(count(8, 5)) # 830