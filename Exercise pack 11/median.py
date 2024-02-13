import heapq

class Median:
    def __init__(self):

        self.r = []
        self.l = []
        self.nleft = 0
        self.nright = 0
        self.n = 0

    def add(self, x):
  
        if self.nleft == 0:
            heapq.heappush(self.l, -x)
            self.nleft += 1

        elif self.nright == 0:
            if x < -self.l[0]:
               heapq.heappush(self.r, -heapq.heappop(self.l))
               heapq.heappush(self.l, -x)
            else:
                heapq.heappush(self.r, x)
            self.nright += 1

        elif self.nright < self.nleft:
            max_left = -heapq.heappop(self.l)
            if x > max_left:
                heapq.heappush(self.r, x)
                heapq.heappush(self.l, -max_left)
            else:
                heapq.heappush(self.r, max_left)
                heapq.heappush(self.l, -x)
            self.nright += 1

        else:
            min_right = heapq.heappop(self.r)
            if min_right < x:
                heapq.heappush(self.r, x)
                heapq.heappush(self.l, -min_right)
            else:
                heapq.heappush(self.l, -x)
                heapq.heappush(self.r, min_right)
            self.nleft += 1

        self.n += 1

    def median(self):
        self.max_left = -heapq.heappop(self.l)
        heapq.heappush(self.l, -self.max_left)
        return self.max_left



if __name__ == "__main__":
    m = Median()
    m.add(10)
    print(m.median())
    m.add(9)
    print(m.median())
    m.add(6)
    print(m.median())
    m.add(10)
    print(m.median())
    m.add(10)
    print(m.median())
    m.add(3)
    print(m.median())
    m.add(6)
    print(m.median())
    m.add(7)
    print(m.median())
    m.add(6)
    print(m.median())
    m.add(5)
    print(m.median())
