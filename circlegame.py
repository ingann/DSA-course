#The circle has n players who are numbered 1,2...,n. The turn goes in roung and every other player gets off from the circle until the circle is empty. The goal is to find the order in which players are getting off. 

#A function returns a list of the order

def create(n):
    circle = [*range(1, n+1)]
    
    rtrn = []
    i = 1

    while len(circle) > 0:
        if len(circle) == 1:
            rtrn.append(circle.pop())
            return rtrn
        last = circle[-1]
        removed = circle[i]
        was_last = False
        rtrn.append(circle.pop(i))
        i += 1
        if i >= len(circle):
            if last == removed:
                was_last = True
            if was_last:
                i = 1
            else:
                i = 0
            was_last = False
    return rtrn


 
if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(7)) # [2,4,6,1,5,3,7]
    print(create(4)) # [2, 4, 3, 1]
    print(create(2)) # [2, 1]
    print(create(6)) # [2, 4, 6, 3, 1, 5]
    print(create(8)) # [2, 4, 6, 8, 3, 7, 5, 1]
    print(create(9)) #[2, 4, 6, 8, 1, 5, 9, 7, 3]
