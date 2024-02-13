class CountPaths:
    def __init__(self, n):
        self.nodes = range(1, n+1)
        self.graph = {node: [] for node in self.nodes}

    def __str__(self):
        return f"{self.graph}"
        
    def add_edge(self, a, b):
        if b not in self.graph[a]:
            self.graph[a].append(b)
        
    def count_from(self, node):
        if node in self.result:
            return self.result[node]
        
        path_count = 0
        for next_node in self.graph[node]:
            path_count += self.count_from(next_node)
        
        self.result[node] = path_count
        return path_count
        
    def count_paths(self, x, y):
        self.result = {y: 1}
        return self.count_from(x)

if __name__ == "__main__":
    c = CountPaths(100)
    for i in range(1, 100):
        c.add_edge(i, 100)

    for i in range (2, 100):
        c.add_edge(1, i)

    c.add_edge(2, 99)
    print(c.count_paths(1, 100))#100