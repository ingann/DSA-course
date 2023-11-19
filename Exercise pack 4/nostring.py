#The goal is to find out how long is the shortest string consisting of characters a-z and is not a part of given string (in a parameter). 
#A function returns the asked length

from random import randint, seed
import itertools

def find(s):
    alphabets = [chr(i) for i in range(ord('a'),ord('z')+1)]
    albets = {}
    for ch in alphabets:
        albets[ch] = 1

    dic = {}
    for cha in s:
        dic[cha] = 1

    round = 1
    while True:
        keywords = [''.join(i) for i in itertools.product(alphabets, repeat = round)]
        for comb in keywords:
            if comb not in s:
                return round
        round += 1
    

if __name__ == "__main__":
    print(find("zzz")) # 1
    print(find("aybabtu")) # 1
    print(find("abcdefghijklmnopqrstuvwxyz")) # 2

    seed(1337)
    h = set()
    s = 'aa'
    for i in range(2, 10**5):
        for u in range(26):
            w = chr(ord('a')+u)
            if s[i-2]+s[i-1]+w not in h:
                h.add(s[i-2]+s[i-1]+w)
                s += w
                break
        if len(s) == i:
            s += chr(ord('a') + randint(0,25))
    print(find(s)) #4

    s = ''
    for i in range(10**5):
        s += chr(ord('a') + randint(0,25))
    print(find(s)) #3
