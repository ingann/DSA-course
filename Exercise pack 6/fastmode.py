#create a class fastmode which has following methods:
#add(x, k): add number x to the list k times
#mode(): most common mode in a list
#both methods has time complexity o(1)

class FastMode:
    def __init__(self):
        self.modes = (0, 0)
        self.exist = {}
 
    def add(self, x, k):
        if x not in self.exist:
            self.exist[x] = k
        else:
            self.exist[x] += k
        
        mode = self.exist[x]
        if mode > self.modes[0]:
            self.modes = (mode, x)
        elif mode == self.modes[0]:
            if x < self.modes[1]:
                self.modes = (mode, x)
        
    def mode(self):
        return self.modes[1]
        

if __name__ == "__main__":
    m = FastMode()
    m.add(4, 7)
    print(m.mode()) # 4
    m.add(8, 5)
    print(m.mode()) # 4
    m.add(8, 3)
    print(m.mode()) # 8
    m.add(4, 1)
    print(m.mode()) # 4
    f = FastMode()
    for i in range(1,10**5+1):
        f.add(i, 10**9)
    print(f.mode())
