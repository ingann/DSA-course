#The program returns the amount of components in a network

class Graph:
    def __init__(self):
        self.n = 1000
        self.graph = {node: [] for node in range(2, 1000 + 1)}
        self.edges()

    def add_edge(self, a, b):
        if a%b == 0 or b%a==0:
            self.graph[a].append(b)
            self.graph[b].append(a)

    def edges(self):
        a = 2
        b = 3
        while b < 1001:
            self.add_edge(a, b)
            b += 1
            if a < 1000 and b == 1001:
                a += 1
                b = a+1
    

    def component(self):
        components = Components(self.graph)
        return components.find_components()
    

class Components:
    def __init__(self, graph):
        self.graph = graph
        
    def visit(self, node):
        if node in self.components:
            return
        self.components[node] = self.counter

        for next_node in self.graph[node]:
            self.visit(next_node)
        
    def find_components(self):
        self.counter = 0
        self.components = {}

        for node in range(2, 1001):
            if node not in self.components:
                self.counter += 1
                self.visit(node)
        return self.counter


if __name__ == "__main__":
    g = Graph()
    print(g.component())
