#create a class repeatlist with following methods:
#add(x): add number x to the list
#check(): return True if there are repeated numbers in a list else return False
#Both methods has time complexity O(1)

class RepeatList:
    def __init__(self):
        self.list = []
        self.repeat = {}
        self.duplicate = False

    def add(self, x):
        self.list.append(x)
        if x in self.repeat:
            self.duplicate = True
        self.repeat[x] = 1


    def check(self):
        return self.duplicate

if __name__ == "__main__":
    r = RepeatList()
    print(r.check()) # False
    r.add(1)
    r.add(2)
    r.add(3)
    print(r.check()) # False
    r.add(2)
    print(r.check()) # True
    r.add(5)
    print(r.check()) # True
