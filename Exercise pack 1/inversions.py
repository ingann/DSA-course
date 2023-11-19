#You are given a list consisting of numbers 1...n. Index pair (i, j) is an inversion if i<j and at list index i there is a bigger number than at index j. 
#A function returns the count of inversions in a list

def count(t):
    inversions = 0
    i = 0 
    j = 0
    indexi = 0
    indexj= 0
    for i in t:
        for j in t:
            if i > j and indexi < indexj:
                inversions += 1
            indexj += 1
        indexi += 1
        indexj = 0

    return inversions

if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([1])) # 0
    print(count([4,3,2,1])) # 6
    print(count([1,8,2,7,3,6,4,5])) # 12
