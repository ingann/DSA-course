#You are given a list with n integers. Create a new list where is every sum of the list's subsets in ascending order. 
import itertools

def create(t):
    result = [0]

    for i in range(1, len(t)+1):
        for combination in itertools.combinations(t, i):
            result.append(sum(combination))
    return sorted(result)
    



if __name__ == "__main__":
    print(create([1, 2, 3])) # [0, 1, 2, 3, 3, 4, 5, 6]
    print(create([42, 1337])) # [0, 42, 1337, 1379]
    print(create([1, 1, 1])) # [0, 1, 1, 1, 2, 2, 2, 3]
    print(create([5])) # [0, 5]
