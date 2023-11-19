#You are given a list where every item is an integer. The goal is to construct a new list where x is added to every item. 

#A function returns the asked list. 

def create(t, x):
    tcopy = [n+x for n in t]
    return tcopy

if __name__ == "__main__":
    print(create([1,2,3],1)) # [2,3,4]
    print(create([1,1,1,1,1],4)) # [5,5,5,5,5]
    print(create([0],10**9)) # [1000000000]
