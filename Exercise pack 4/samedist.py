#You are given a list where are n integers. The goal is to find the biggest distance between the same numbers. Distance means the difference of indexes. 
#Time complexity for this algorithm is O(n)
#A function returns the asked distance

def find(t):

    pos = {}
    found = False
    result = 0

    for i, no in enumerate(t):
        if no in pos:
            pos[no].append(i)
            found = True
        else:
            pos[no] = [i]

    result = 0

    for key in pos:
        result = max(result, (max(pos[key])-min(pos[key])))

    if found:
        return result
    return 0
    
    

if __name__ == "__main__":
    print(find([1,2,1,1,2])) # 3
    print(find([1,2,3,4])) # 0
    print(find([1,1,1,1,1])) # 4
    print(find([1,1,2,3,4])) # 1
    print(find([1,5,1,5,1])) # 4
    print(find([9, 6, 10, 10, 3])) #1
