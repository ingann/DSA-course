#a list contains integers 1...n. In how many ways tou can choose k numbers from the list so that their sum is x? You can assume 1<=n<=10 and 1<=k<=n. 
import itertools
def count(n, k, x):
    list = [*range(1, n+1)]
    result = 0
    for combination in itertools.combinations(list, k):
        if sum(combination) == x:
            result += 1
    return result

if __name__ == "__main__":
    print(count(1, 1, 1)) # 1
    print(count(5, 2, 6)) # 2
    print(count(8, 3, 12)) # 6
    print(count(10, 4, 20)) # 16
