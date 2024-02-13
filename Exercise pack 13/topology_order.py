class TopologicalSort:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.graph = {node: [] for node in self.nodes}
        
    def add_edge(self, a, b):
        self.graph[a].append(b)
        
    def visit(self, node):
        if self.state[node] == 1:
            self.cycle = True
            return
        if self.state[node] == 2:
            return

        self.state[node] = 1
        for next_node in self.graph[node]:
            self.visit(next_node)

        self.state[node] = 2
        self.order.append(node)
        
    def create(self):
        self.state = {}
        for node in self.nodes:
            self.state[node] = 0

        self.order = []
        self.cycle = False
        
        for node in self.nodes:
            if self.state[node] == 0:
                self.visit(node)
                
        if self.cycle:
            return None
        else:
            self.order.reverse()
            return self.order        

if __name__ =="__main__":
    t = TopologicalSort(6)

    t.add_edge(1, 2)
    t.add_edge(2, 3)
    t.add_edge(3, 6)
    t.add_edge(4, 1)
    t.add_edge(4, 5)
    t.add_edge(5, 2)
    t.add_edge(5, 3)

    print(t.create()) # [4, 5, 1, 2, 3, 6]