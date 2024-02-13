class Components:
    def __init__(self, n):
        self.link = {node: None for node in range(1, n + 1)}
        self.size = {node: 1 for node in range(1, n + 1)}

    def add_road(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return
 
        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]  

    def find(self, x):
        while self.link[x]:
            x = self.link[x]
        return x

    def count(self):
        result = set()
        for node in self.link:
            result.add(self.find(node))
        return len(result)

if __name__ == "__main__":
    c = Components(5)
    print(c.count()) # 5
    c.add_road(1, 2)
    c.add_road(1, 3)
    print(c.count()) # 3
    c.add_road(2, 3)
    print(c.count()) # 3
    c.add_road(4, 5)
    print(c.count()) # 2