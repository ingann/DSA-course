def count(t):
    t.sort()
    tset = {}
    for item in t:
        if item not in tset:
            tset[item] = 1
    
    length = 1
    biggest = 1
    diff = -2

    for n in tset:
        if n-diff == 1:
            length += 1
            if length > biggest:
                biggest = length
        else:
            length = 1
        diff = n
        
    return biggest

if __name__ == "__main__":
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3
    print(count([14, 15, 16, 15, 13])) # 4