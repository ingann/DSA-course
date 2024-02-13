#You are given n coins and sum x. The goal is to count the biggest amount of coins to get given sum.
#The function returns a count for max amount of coins.
#I utilized this code in my solution: https://www.geeksforgeeks.org/maximize-count-of-array-elements-required-to-obtain-given-sum/

def find(x, coins):

    n = len(coins)

    table = [0 for i in range(x+1)]
 
    # Base Case
    table[0] = 0
 
    # Initialize all table values
    for i in range(1, x + 1):
        table[i] = -1
 
        # Find the max coins required
        # for all values from 1 to x
        for i in range(1, x + 1, 1):
 
        # Go through all coins
        # smaller than i
            for j in range(0, n, 1):

                # If current coin value
                # is less than i
                if (coins[j] <= i):
                    left = table[i - coins[j]]

                    # Update table[i]
                    if (left != -1 and
                        left + 1 > table[i]):
                        table[i] = left + 1

    return table[x]
    
if __name__ == "__main__":
    print(find(13, [1, 2, 5])) # 13
    print(find(13, [2, 3, 5])) # 6
    print(find(13, [2, 4, 6])) # -1
    print(find(42, [8, 9, 11, 15])) # 5
    print(find(30, [5, 10, 25])) #6