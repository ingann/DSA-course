#You are given a string of bits (0 and 1). The goal is to count in how many ways can you choose two points so that both points in the string has the same bit. 
#time complexity for this algorithm is O(n)
#A function returns the asked result


def count(s):
    zeros = 0
    ones = 0

    for bit in s:
        if bit == "0":
            zeros += 1
        else:
            ones += 1

    return counter(zeros)+counter(ones)
    
def counter(n):
    counts = 0
    n -= 1
    while n > 0:
        counts += n
        n -= 1
    return counts
        

if __name__ == "__main__":
    print(count("0101")) # 2
    print(count("000000")) # 15
    print(count("000111")) # 6
    print(count("00100001101100")) # 46
