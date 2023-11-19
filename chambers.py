#You are given and nxm grid presenting a house's floor plan. Every square is either floor(.) or wall (#) and every square in the edge of a grid is wall. Two floor squares belong to the same room if they are adjacent in horizontal or vertical way. How many rooms are there in a house?
#The function returns the amount of rooms

def count(r):
    G = []
    ro = []
    ro_no = 0
    i = 1
    numbers = {}
    adjacent = 1
 
    for row in r:
        for cha in row:
            if cha == "#":
                ro.append(0)
                adjacent = 1
            else:
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
 
    comp = simplified(edges, G)

    rooms = 0
    for nro in G:
        if nro not in edges:
            rooms += 1
 
    comps = Components(comp)
    rooms += comps.find_components()
    return rooms
 
def simplified(graph, n):
    eqs = {}
    i = 1
    for no in n:
        eqs[no] = i
        i += 1
    
    comp = {}
    
    for key in graph:
        comp[eqs[key]] = []
        for value in graph[key]:
            val = eqs[value]
            comp[eqs[key]].append(val)
    return comp
 
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
 
class Components:
    def __init__(self, graph):
        self.n = len(graph)
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
 
        for node in range(1, self.n + 1):
            if node not in self.components:
                self.counter += 1
                self.visit(node)
        return self.counter
 
 
 
 
if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3

    r = ["##########",
        "##########",
        "##########",
        "##########",
        "#####.####",
        "##########",
        "##########",
        "##########",
        "##########",
        "##########"]
    print(count(r)) # 
