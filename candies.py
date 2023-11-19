#How many candies you can buy if you have x amount of money. Candy1 costs a euros and candy2 costs b euros. 
#A function returns the biggest amount of candies you can buy.

def count(a, b, c):
    amount = 0
    if a < b:
        while c >= a:
            c -= a
            amount += 1
    else:
        while c >= b:
            c -= b
            amount += 1
    return amount

if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4
