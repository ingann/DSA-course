#Network has n computers with no edges to each other. Create a class where you can add an edge between two computers and find the shortest route between two computers. 

class Network:
    def __init__(self,n):
        self.n = n
        self.graph = {node: [] for node in range(1, n+ 1)}

    def add_link(self,a,b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def best_route(self,a,b):
        if self.has_route(a, b):
            paths = ShortestPaths(self.graph)
            shortest = paths.find_paths(a)
            return shortest[b]
        else:
            return -1

    def has_route(self,a,b):
        bfs = BFS(self.graph)
        visited = bfs.search(a)
        if b in visited:
            return True
        return False

class BFS:
    def __init__(self, graph):
        self.graph = graph

    def search(self, start_node):
        self.visited = set()

        queue = [start_node]
        self.visited.add(start_node)

        for node in queue:
            for next_node in self.graph[node]:
                if next_node not in self.visited:
                    queue.append(next_node)
                    self.visited.add(next_node)
        return self.visited
    
class ShortestPaths:
    def __init__(self, graph):
        self.graph = graph

    def find_paths(self, start_node):
        self.distances = {}
        self.previous = {}

        self.distances[start_node] = 0
        self.previous[start_node] = None
        queue = [start_node]

        for node in queue:
            distance = self.distances[node]
            for next_node in self.graph[node]:
                if next_node not in self.distances:
                    self.distances[next_node] = distance + 1
                    self.previous[next_node] = node
                    queue.append(next_node)
        return self.distances


if __name__ == "__main__":
    w = Network(5)
    w.add_link(1,2)
    w.add_link(2,3)
    w.add_link(1,3)
    w.add_link(4,5)
    print(w.best_route(1,5)) # -1
    w.add_link(3,5)
    print(w.best_route(1,5)) # 2
