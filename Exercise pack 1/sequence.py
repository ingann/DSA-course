#Every item in a sequence is a smallest positive integers which is not yet found in the sequence and has one or more repeated number. 
#The sequence starts like this: 11, 22, 33, 44...
#The goal is to find a number at place n. A function returns the asked integer at place n. 

def generate(n):
    sequence = []
    position = n
    i = 0
    while len(sequence) <= position:
        for cha in str(i):
            times = str(i).count(cha)
            if times >= 2 and i not in sequence:
                sequence.append(i)
        i += 1
    return sequence[position-1]

if __name__ == "__main__":
    print(generate(1)) # 11
    print(generate(2)) # 22
    print(generate(3)) # 33
    
    print(generate(10)) # 100
    print(generate(123)) # 505
