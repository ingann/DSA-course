#You are given a list with n integers. The goal is to count the amount of increasing subsequences in a list
#The function returns the count of subsequences. You can assume 0>=N>=100
#I utilized this solution in my code: https://www.geeksforgeeks.org/count-all-increasing-subsequences/

def count(t):

    n = len(t)
    #initialize the count array to zeros, 0>=n>=100
    count = [0 for i in range(101)]
 
    # scan each number in t[]
    for i in range(n):
     
        # count all possible sub-sequences by
        # the digits less than t[i] digit
        for j in range(t[i] - 1, -1, -1):
            count[t[i]] += count[j]
 
        # store sum of all sub-sequences 
        # plus 1 in count[] array
        count[t[i]] += 1
     
 
    # Now sum up the all sequences 
    # possible in count[] array
    result = 0
    for i in range(101):
        result += count[i]
 
    return result
 

if __name__ == "__main__":
    print(count([1, 1, 2, 2, 3, 3])) # 26
    print(count([1, 1, 1, 1])) # 4
    print(count([5, 4, 3, 2, 1])) # 5
    print(count([4, 1, 5, 6, 3, 4, 1, 8])) # 37
    print(count([86, 98, 22, 50, 97, 57, 85, 75, 59, 99, 71, 27, 2, 60, 64, 72, 90, 90, 90, 67, 87, 6, 62, 68, 27, 100, 85, 5, 71, 82, 36, 64, 88, 43, 53, 82, 81, 51, 52, 87, 9]))#14937