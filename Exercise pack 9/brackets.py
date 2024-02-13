#count how many bracketed terms is able to construct from n brackets so that there are at most k brackets nested
import itertools
def count(n, k):
    result = count_sequences(n, k)
    return result

def count_sequences(n, k, d=0):
    if d < 0 or d > n or d > k:
        return 0
    if n == 0:
        return 1
    return count_sequences(n - 1, k, d + 1) + \
           count_sequences(n - 1, k, d - 1)



if __name__ == "__main__":
    print(count(6, 1)) # 1
    print(count(6, 2)) # 4
    print(count(6, 3)) # 5
    print(count(9, 1)) # 0
    print(count(16, 4)) # 1094
