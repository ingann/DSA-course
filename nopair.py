#You are given a list where are n integers. There are two times each number but only one number is present only once. The goal is to find this number. 
#Time complexity for this algorithm is O(n)
#A function returns the asked integer

def find(t):
    dic = {}
    for n in t:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
    for key in dic:
        if dic[key] == 1:
            return key

if __name__ == "__main__":
    print(find([2,1,3,2,3])) # 1
    print(find([5,5,9])) # 9
    print(find([1,2,3,4,1,3,4])) # 2
    print(find([8])) # 8
    print(find([7,1,7,4,4,5,1])) # 5
