#I utilized this code in my solution: https://www.geeksforgeeks.org/count-of-ways-to-empty-given-string-by-recursively-removing-all-adjacent-duplicates/
  
# Recursive function to calculate the dp 
# values for range [left, right] 
def calc(l, r, s, dp, choose) : 
  
    # The range is odd length 
    if (abs(r - l) % 2 == 0) : 
        return 0; 
  
    if (l > r) : 
        dp[l][r] = 1
        return dp[l][r] 
  
    # The state is already calculated 
    if dp[l][r] != -1: 
        return dp[l][r]
  
    # If the length is 2 
    if ((r - l) == 1) : 
        if (s[l] == s[r]): 
            dp[l][r] = 1 
          
        else : 
            dp[l][r] = 0 
          
        return dp[l][r] 
      
    # Total answer for this state 
    result = 0
      
    for k in range(l + 1, r + 1, 2) : 
  
        # Variable to store the current answer. 
        temp = 1; 
  
        # Remove characters s[l] and s[i]. 
        if s[l] == s[k]: 
            temp = calc(l + 1, k - 1, s, dp, choose) * calc(k + 1, r, s, dp, choose) * choose[(r - l + 1) // 2][(r - k) // 2]; 
            result += temp; 
          
      
    dp[l][r] = result; 
    return dp[l][r] 
  
def count(S) : 

    #define dp and choose matrices
    dp = [0]*100
    choose = [0]*100
    for x in range(100):
        dp[x] = [0]*100

    for x in range(100):
        choose[x] = [0]*100
 
    # Initialize all the states of dp to -1 
    for i in range(100): 
        for j in range(100) : 
            dp[i][j] = -1
  
    # Calculate all Combinations 
    n = len(S); 
    choose[0][0] = 1; 
    for i in range(1, (n // 2) + 1) :  
        choose[i][0] = 1; 
        for j in range(1, i + 1) : 
            choose[i][j]= choose[i - 1][j] + choose[i - 1][j - 1]; 
      
    return calc(0, n - 1, S, dp, choose)


    
if __name__ == "__main__":
    print(count("1100")) # 2
    print(count("1001")) # 1
    print(count("100111")) # 5
    print(count("11001")) # 0
    print(count("1100110011100111")) # 113925