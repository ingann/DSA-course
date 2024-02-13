class MaxSet:
    def __init__(self, n):
        self.graph = UnionFind(n)

    def merge(self, a, b):
        self.graph.union(a, b)

    def get_max(self):
        return self.graph.max

class UnionFind:
    def __init__(self, n):
        self.link = {node: None for node in range(1, n + 1)}
        self.size = {node: 1 for node in range(1, n + 1)}
        self.max = self.size[n]
            
    def find(self, x):
        while self.link[x]:
            x = self.link[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return
 
        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]   
        if self.size[b] > self.max:
            self.max = self.size[b] 


if __name__ == "__main__":
    m = MaxSet(5)
    print(m.get_max()) # 1
    m.merge(1, 2)
    m.merge(3, 4)
    m.merge(3, 5)
    print(m.get_max()) # 3
    m.merge(1, 5)
    print(m.get_max()) # 5
    print()
    m = MaxSet(5)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(3,4)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(2,4)