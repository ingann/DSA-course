#You are given a nxm grid presenting a labyrinth. The goal is to count the length of a shortest route from square A to square B. Every square is either floor(.) or wall(#) and every square at the edge of a square is wall. 
#The function returns a length of the shortest route

def count(r):
    G = []
    ro = []
    ro_no = 0
    i = 1
    numbers = {}
    adjacent = 1
    ab = {}
 
    for row in r:
        for cha in row:
            if cha == "#":
                ro.append(0)
                adjacent = 1
            else:
                if cha == "A" or cha == "B":
                    ab[cha] = i
                ro.append(i)
                G.append(i)
                adjacent += 1
                numbers[i] = [ro_no]
            i += 1
        ro = []
        ro_no += 1
 
    n=len(r[0])
    rounds = 0
    i = 0
    edges = {}
 
    while i < len(G)-1:
        edges = add_edge(numbers, edges, G[i], G[i+1], n)
        i += 1
        rounds += 1

    if has_route(edges, ab["A"], ab["B"]):
        return best_route(edges, ab["A"], ab["B"])
    else:
        return -1

def best_route(graph,a,b):
        paths = ShortestPaths(graph)
        shortest = paths.find_paths(a)
        return shortest[b]
 
def add_edge(graph, edges, a, b, n):
    row1 = graph[a]
    row2 = graph[b]
    if a not in edges:
        edges[a] = []
    if b not in edges:
        edges[b] = []
 
    if a+n in graph:
        if a+n not in edges:
            edges[a+n] = []
        edges[a].append(a+n)
        edges[a+n].append(a)
    if a+1 == b or a-1 == b:
        if row1 == row2:
            edges[a].append(b)
            edges[b].append(a)
    return edges

def has_route(graph, a,b):
        bfs = BFS(graph)
        visited = bfs.search(a)
        if b in visited:
            return True
        return False

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
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7
