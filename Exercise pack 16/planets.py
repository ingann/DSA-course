class Planets:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0
        
        self.n = n

    def add_teleport(self, a, b):
        self.graph[(a, b)] += 1

    def add_flow(self, node, sink, flow):
        if node in self.seen:
            return 0
        self.seen.add(node)
        if node == sink:
            return flow
        for next_node in self.nodes:
            if self.flow[(node, next_node)] > 0:
                new_flow = min(flow, self.flow[(node, next_node)])
                inc = self.add_flow(next_node, sink, new_flow)
                if inc > 0:
                    self.flow[(node, next_node)] -= inc
                    self.flow[(next_node, node)] += inc
                    return inc
        return 0

    def calculate(self):
        a = 1
        b = self.n
        self.flow = self.graph.copy()
        total = 0
        while True:
            self.seen = set()
            add = self.add_flow(a, b, float("inf"))
            if add == 0:
                break
            total += add
        return total

if __name__ == "__main__":
    p = Planets(5)
    print(p.calculate()) # 0
    p.add_teleport(1, 2)
    p.add_teleport(2, 5)
    print(p.calculate()) # 1
    p.add_teleport(1, 5)
    print(p.calculate()) # 2