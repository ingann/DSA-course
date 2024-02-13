import itertools
def count(x):
    coins = 0
    for coin in [5, 2, 1]:
        tuple = counter(x, coin)
        x = tuple[0]
        coins += tuple[1]
    return coins

def counter(x, coin):
    remainder = x%coin
    coins = x//coin
    if remainder < 0:
        return (x, 0)
    else:
        return (x-coins*coin, coins)

if __name__ == "__main__":
    print(count(13)) # 4
    print(count(12345)) # 2469
    print(count(1337**9)) # 2730314408854633746890878156