#You are given a list where are n integers. The goal is to count in how many ways can you split a list so that the smallest number of both parts in a list is the same. 
#Time complexity for this algorithm is O(n)
#A function returns the asked result 

def count(t):
    smallest = min(t)
    
    i = 0
    scount = 0
    indexes = {}
    count = 0

    while i < len(t):
        if t[i] == smallest:
            scount += 1
            indexes[scount] = i
            if scount > 1:
                count += indexes[scount]-indexes[scount-1]
        i += 1

    return count
        

if __name__ == "__main__":
    print(count([2,1,1,3])) # 1
    print(count([1,1,1,1])) # 3
    print(count([1,2,3,1,2,3])) # 3
    print(count([1,2,3,4,3,2,1])) # 6
    print(count([4,3,2,1,2,3,4])) # 0
    print(count([3, 2, 5, 1, 5, 5, 5, 1, 1, 4])) #5
