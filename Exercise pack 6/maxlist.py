#create a class maxlist with following methods:
#add(x): add number x to the list
#max(): return biggest number in a list (or None if empty)
#Time complexoty for methods are o(1)

class MaxList:
    def __init__(self):
        self.list = []
        self.biggest = 0


    def add(self, x):
        self.list.append(x)
        if x > self.biggest:
            self.biggest = x

    def max(self):
        if self.list == []:
            return None
        return self.biggest
        

if __name__ == "__main__":
    m = MaxList()
    print(m.max()) # None
    m.add(1)
    m.add(2)
    m.add(3)
    print(m.max()) # 3
    m.add(8)
    m.add(5)
    print(m.max()) # 8
