#You are given a string where every character is 0 or 1 (bits). The goal is to change the string so that every bit is the same. What is the smallest amount of changes required=
#A function returns the count of changes required

def count(s):
    ones = 0
    zeros = 0

    for n in s:
        if n == "1":
            ones += 1
        else:
            zeros += 1
    
    if ones == 0 or zeros == 0:
        return 0 
    elif ones < zeros:
        return ones
    else:
        return zeros
    

if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4
