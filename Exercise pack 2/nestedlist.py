#The goal is to count how many numbers there are in the given list. List may have items as lists which may have also items as lists. A list has items as numbers or/and lists. 
#A function returns the amount of numbers in a list.  

def count(t):
    counts = 0
    lists = []

    for item in t:
        if (item.__class__ == list):
            lists.append(item)
        else:
            counts += 1

    counts += list_traverse(lists)

    return counts

def list_traverse(l):
    counts = 0
    i = 0
    while i < len(l):
        if (l[i].__class__ == list):
            counts += list_traverse(l[i])
        else:
            counts += 1
        i += 1

    return counts
        

if __name__ == "__main__":
    print(count([1,2,3])) # 3
    print(count([1,[2,3],4,5,[6]])) # 6
    print(count([1,[1,[1,[1]]]])) # 4
    print(count([[1,2,[3,4]],5,[[6,[7],8]]])) # 8
