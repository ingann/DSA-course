
#You are given a list with n integers. The goal is to find biggest ascending subsequence in the array. 
#The function can return any suitable subsequence if there are multiple solutions.  
#I utilized this solution in my code: https://www.geeksforgeeks.org/construction-of-longest-monotonically-increasing-subsequence-n-log-n/
def GetMaxIndex(t, tails, l, length, number):
 
    while length - l > 1:
     
        m = l + (length - l)//2
        if t[tails[m]] >= number:
            length = m
        else:
            l = m
 
    return length

def find(t):
    n = len(t)

    tails =[0 for i in range(n + 1)]  
 
 
    prevs =[-1 for i in range(n + 1)]  
     
    length = 1
    for i in range(1, n):
     
        #new smallest value
        if t[i] <= t[tails[0]]:
            tails[0] = i
         
        #elif there is even bigger value, extending the longest subsequence
        elif t[i] > t[tails[length-1]]:
            prevs[i] = tails[length-1]
            tails[length] = i
            length += 1
         
        else:
            option = GetMaxIndex(t, tails, -1,
                                   length-1, t[i])
            prevs[i] = tails[option-1]
            tails[option] = i
         
    result = []
    i = tails[length-1]
    while i >= 0:
        result.append(t[i])
        i = prevs[i]
    return sorted(result)

if __name__ == "__main__":
    print(find([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find([1, 1, 1, 1])) # [1]
    print(find([5, 4, 3, 2, 1])) # [3]
    print(find([4, 1, 5, 6, 3, 4, 1, 8])) # [1, 3, 4, 8]
    print(find([6, 1, 1, 9, 10, 4, 7, 5, 9, 6]))
    print(find([3, 1, 8, 10, 8, 1, 9, 8, 9]))