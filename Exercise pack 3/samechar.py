#The goal is to count how many substrings of a string consist of same characters.
#Time complexity for this algorithm is O(n)
#A function returns the asked result

#I utilized this solution in my code: https://www.geeksforgeeks.org/count-number-of-substrings-of-a-string-consisting-of-same-characters/

def count(s):

    count = 1
    result = 0

    b = 0 #start
    e = 1 #end

    while e < len(s):
        if s[b] == s[e]:
            count += 1

        else:
            result += count*(count+1)//2
            b = e
            count = 1
        e += 1

    result += count*(count+1)//2
    return result
    
if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5
