import collections

class FlipList:
    def __init__(self):
        self.l = collections.deque()
        self.flippedL = collections.deque()

    def push_first(self,x):
        self.l.appendleft(x)
        self.flippedL.append(x)

    def push_last(self,x):
        self.l.append(x)
        self.flippedL.appendleft(x)

    def pop_first(self):
        self.flippedL.pop()
        return self.l.popleft()

    def pop_last(self):
        self.flippedL.popleft()
        return self.l.pop()

    def flip(self):
        default = self.l
        flipped = self.flippedL
        self.l = flipped
        self.flippedL = default

if __name__ == "__main__":
    f = FlipList()
    f.push_last(1)
    f.push_last(2)
    f.push_last(3)
    print(f.pop_first()) # 1
    f.flip()
    print(f.pop_first()) # 3