#The goal is to count how many substrings of a string has no a-character. 
#Time complexity for this algorithm is O(n)
#A function returns the asked result

#I utilized this solution in my code: https://www.geeksforgeeks.org/count-of-sub-strings-that-contain-character-x-at-least-once/

def count(s):


    result = 0
    count = 0

    n = len(s)

    total_substrings = n*(n+1)//2

    for i in range(n):
        if s[i] == "a":
            result += ((count+1)*(n-i))
            count = 0
        else:
            count += 1
    return total_substrings-result


if __name__ == "__main__":
    print(count("aaa")) # 0
    print(count("saippuakauppias")) # 23
    print(count("x")) # 1
    print(count("aybabtu")) # 9
