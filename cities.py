#A world has n cities with no edges to each other. Create a class where you can add an edge between two cities and return True if there is a route from city a to city b.

class Cities:
    def __init__(self,n):
        self.n = n
        self.graph = {node: [] for node in range(1, n+ 1)}

    def add_road(self,a,b):
        self.graph[a].append(b)
        self.graph[b].append(a)

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



if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1,2)
    c.add_road(1,3)
    c.add_road(4,5)
    print(c.has_route(1,5)) # False
    c.add_road(3,4)
    print(c.has_route(1,5)) # True

    print("onni, ilo, autuus")
