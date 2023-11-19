#create a class quicklist with following methods:
#move(k): move first k items in a list to the end of the list
#get(i): return item at index i
#Time complexity for the methods is O(1)

class QuickList:
    def __init__(self, t):
        self.array = t
        self.rounds = 0
        self.counts = 0
        self.n = len(self.array)
   
    def move(self, k):

        self.counts += k
        if self.counts >= self.n:
            self.rounds += 1
            self.counts -= self.n
        
    def get(self, i):
        i += self.counts
        if i >= self.n:
            i -=self.n
        return self.array[i]

if __name__ == "__main__":
    q = QuickList([1,2,3,4,5,6,7,8,9,10])
    print(q.get(4)) # 5
    q.move(3)
    print(q.get(4)) # 8
    q.move(3)
    print(q.get(4)) # 1
    q.move(10)
    print(q.get(4)) # 1
    q.move(7)
    q.move(5)
    print(q.get(0)) # 9
