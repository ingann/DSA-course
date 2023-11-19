#The goal is to find out how long is the smallest string that when repeated you can construct the given string (given as parameter). E.g. when the string is abcabcabc the smallest string to repeat is abc. 

#A function returns the length of the smallest string which is repeated. 

 def find(s):
    repeats = s[0]
    found = False
    i = 1
    next = len(repeats)
    while not found:
        if i == len(s):
            found = True
            return len(repeats)
        elif repeats in s[next:2*next]:
            times = len(s)/len(repeats)
            if len(s)%len(repeats) == 0 and repeats*int(times) == s:
                found = True
                return len(repeats)
        repeats += s[i]
        i += 1
        next = len(repeats)

    print(repeats)
    return len(repeats)

if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7
