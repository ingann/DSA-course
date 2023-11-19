#You are given the price of a stock of n days. The goal is to find out what is the biggest profit you could have gotten if you had a chance to buy and sell the stock two times at max. You can only hold one stock at a time. 
#Time complexity for this algorithm is O(n)
#A function returns the asked result

#I utilized this solution in my code: https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/

def find(t):

    n = len(t)

    profit = [0]*n #initialize the profit array to zeroes
    max_price = t[-1] #max prize at the end of prices array t

    for i in range(n-2, 0, -1): #for loop in reverse order
 
        if t[i] > max_price:
            max_price = t[i]
            
        profit[i] = max(profit[i+1], max_price - t[i]) #max profit, comparing the previous value which is the max profit at the moment 
 
    #max profit when there is at most two transactions
    min_price = t[0]
    i = 0
    while i < n:
 
        if t[i] < min_price:
            min_price = t[i]
        profit[i] = max(profit[i-1], profit[i]+(t[i]-min_price)) #max profit, comparing previous value and current price if selling at current price when bought with min cost
        i += 1
 
    result = profit[-1]
 
    return result
 

if __name__ == "__main__":
    print(find([1,5,1,5])) # 8
    print(find([1,2,3,4,5])) # 4
    print(find([5,4,3,2,1])) # 0
    print(find([4,2,5,8,7,6,1,2,5,1])) # 10
