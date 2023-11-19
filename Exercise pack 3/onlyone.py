#You are given a list where are n integers. Numbers n-1 are the same and then there is one other number in a list which is present only once in this list. 
#Time complexity for this algorithm is O(n)
#A function returns the asked result


def find(t):
     
    n = t.count(t[0])

    if n == 1:
        return t[0]
    
    for i in t:
        if i != t[0]:
            return i
     


if __name__ == "__main__":
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5
