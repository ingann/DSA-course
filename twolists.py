#You are given two lists A and B which both consists of numbers 1..n in some order. The goal is to count how many of these numbers is present in list A before the number is present in list B. Time complexity for this algorithm is O(n). 

#A function returns the count of numbers that is present in list A earlier than in list B. 

def count(a, b):
    if len(a) == 1:
        return 0
    
    adict = {}
    i = 0
    for n in a:
        adict[n] = i
        i += 1
    
    counts = 0
    i = 0
    for number in b:
        if adict[number] < i:
            counts += 1
        i += 1
        
    return counts



if __name__ == "__main__":
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([1,2,3,4], [1,2,3,4])) # 0
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5
