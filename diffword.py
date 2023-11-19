#You are given a string which has words that are differentiated with spaces. The goal is to efficiently count how many words there are in the string. 
#A function returns the word count

def count(s):
   
    seen = {}
    word = ""
    for ch in s:
        if ch == " ":
            if word not in seen:
                seen[word] = 1
            word = ""
            continue
        word += ch
    if word not in seen:
        seen[word] = True
    
    return len(seen)
    


if __name__ == "__main__":
    print(count("apina apina apina")) # 1
    print(count("apina banaani cembalo")) # 3
    print(count("a b c a b c a b c")) # 3
    print(count("saippuakauppias")) # 1
