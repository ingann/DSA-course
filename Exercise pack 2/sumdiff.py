#Construct a list which has numbers 1...n and every number next to each other has different sum than the next two numbers. 
#A function returns the asked list

def create(n):
    numbers = [*range(1, n+1)]
    return numbers
        

if __name__ == "__main__":
    print(create(6)) # [3, 1, 6, 2, 4, 5]
    print(create(10)) # [7, 10, 3, 1, 5, 4, 8, 6, 9, 2]
    print(create(15)) # [9, 4, 6, 14, 15, 13, 12, 11, 5, 2, 3, 8, 1, 7, 10]
