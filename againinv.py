#The goal is to construct a list of numbers 1...n which has exactly k inversions. 
#A function returns a list which has k amount of inversions.

def create(n, k):
    t = list(range(1, n+1))
    if k == 0:
        return t

    max = t[-1]
    i = n-2
    start = 0
    invs = 0

    while invs < k:
        if t[i] < max:
            change = t[i]
            t[i] = max
            t[i+1] = change
            invs += 1
        if t[start] == max:
            max = t[-1]
            i = n-1
            start += 1
        i -= 1
    return t


if __name__ == "__main__":
    print(create(3, 0)) # [1,2,3]
    print(create(3, 1)) # esim. [1,3,2]
    print(create(3, 2)) # esim. [3,1,2]
    print(create(9, 34))
