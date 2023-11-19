#create a class mex with following methods:
#add(x): add integer x to the list and return the mex-number of a list
#mex is the smallest positive integer that is not present in the list
#Method has a time complexity O(1)

class Mex:
    def __init__(self):
        self.mex = {}
        self.smallest = 0
        self.smallest_list = 0

    def add(self, x):
        if x not in self.mex:
            self.mex[x] = 1
        if x < self.smallest_list:
            self.smallest_list = x

        if self.smallest_list <= self.smallest:
            while self.smallest in self.mex:
                self.smallest += 1
        return self.smallest

if __name__ == "__main__":
    m = Mex()
    print(m.add(1)) # 0
    print(m.add(3)) # 0
    print(m.add(4)) # 0
    print(m.add(0)) # 2
    print(m.add(5)) # 2
    print(m.add(2)) # 6
