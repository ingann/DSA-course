class Ball:
    def __init__(self, n):
        self.nodes = range(1, (n*2) + 3)
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0
        
        for no in range(2, n+2):
            self.graph[(1, no)] = 1
        
        for no in range(n+2, (n*2)+2):
            self.graph[(no, (n*2)+2)] = 1
        
        self.n = n

    def add_pair(self, a, b):
        self.graph[(a+1, b+self.n+1)] += 1

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
        b = (self.n*2)+2
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
    b = Ball(4)
    print(b.calculate()) # 0
    b.add_pair(1, 2)
    print(b.calculate()) # 1
    b.add_pair(1, 3)
    b.add_pair(3, 2)
    print(b.calculate()) # 2
