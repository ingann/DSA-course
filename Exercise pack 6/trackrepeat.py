#create a class trackrepeat with following methods:
#add(x, k): add number x to the list k times
#check(): return True if every number in the list is repeated different amounts else return False
#Time complexity for the methods is O(1)

class TrackRepeat:
    def __init__(self):
        self.numbers = {}
        self.duplicates = {}

 
    def add(self, x, k):
        if x not in self.numbers:
            self.numbers[x] = 0        
        self.numbers[x] += k
        
        curr = self.numbers[x]
        prev = self.numbers[x]-k
        self.check_doubles(curr, prev, x)

    def check_doubles(self, curr, prev, x):
        
        if prev in self.duplicates:
            self.duplicates[prev] -= 1
            if self.duplicates[prev] == 0:
                del self.duplicates[prev]
    
        if curr not in self.duplicates:
            self.duplicates[curr] = 0
        self.duplicates[curr] += 1
 
    def check(self):
        return len(self.duplicates) == len(self.numbers)
    
if __name__ == "__main__":
    t = TrackRepeat()
    print(t.check()) # True
    t.add(1, 3)
    print(t.check()) # True
    t.add(2, 3)
    print(t.check()) # False
    t.add(2, 2)
    print(t.check()) # True
    t.add(3, 1)
    print(t.check()) # True
    t.add(3, 4)
    print(t.check()) # False
 
    print()
    t = TrackRepeat()
    t.add(10, 9)
    print(t.check())
    t.add(6, 10)
    print(t.check())
    t.add(10, 3)
    print(t.check())
    t.add(6, 7)
    print(t.check())
    t.add(6, 5)
    print(t.check())
    t.add(7, 4)
    print(t.check())
    t.add(6, 2)
    print(t.check())
    t.add(7, 7)
    print(t.check())
    t.add(2, 9)
    print(t.check()) #True
    t.add(6, 7)
    print(t.check())

    print()
    t = TrackRepeat()
    t.add(7, 5)
    print(t.check())
    t.add(1, 6)
    print(t.check())
    t.add(10, 2)
    print(t.check())
    t.add(8, 4)
    print(t.check())
    t.add(3, 6)
    print(t.check()) #False
    t.add(10, 8)
    print(t.check()) #False
    t.add(10, 5)
    print(t.check())
    t.add(4, 9)
    print(t.check())
    t.add(2, 9)
    print(t.check())
    t.add(10, 10)
    print(t.check())
