import heapq
def count(r):

    n = len(r[0]*len(r))
    graph = Dijkstra(n)

    t = []
    for row in r:
        for col in row:
            t.append(col)
    rlen = len(r[0])
    current_row = rlen

    for i in range(n):
        if i-1 >= 0:
            if i != current_row-rlen:
                graph.add_edge(i, i-1, t[i-1])
        if i+1 < current_row:
            graph.add_edge(i, i+1, t[i+1])
        if i+rlen < n:
            graph.add_edge(i, i+rlen, t[i+rlen])
        if i-rlen >= 0:
            graph.add_edge(i, i-rlen, t[i-rlen])
        if i == current_row-1:
            current_row += rlen

    return graph.find_distances(0)+t[0]

class Dijkstra:
    def __init__(self, n):
        self.nodes = range(n)
        self.graph = {node: [] for node in range(0, n)}
    
    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))
    
    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0
        
        queue = []
        heapq.heappush(queue, (0, start_node))
        
        visited = set()
        while queue:
            node_a = heapq.heappop(queue)[1]
            if node_a in visited:
                continue
            visited.add(node_a)

            for node_b, weight in self.graph[node_a]:
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    new_pair = (new_distance, node_b)
                    heapq.heappush(queue, new_pair)

        print(self.graph)
        return distances[len(self.graph)-1]

if __name__ == "__main__":
    r = [[2, 1, 4, 8],
         [3, 8, 7, 2],
         [9, 5, 1, 2]]
    print(count(r)) # 17

    g = [[6, 7, 6], 
         [5, 7, 4], 
         [6, 2, 7], 
         [7, 2, 9], 
         [6, 7, 7], 
         [5, 1, 6]]
    print(count(g))#35

    d = [[4, 3, 6, 10, 8, 10, 5, 4],
        [9, 2, 9, 10, 10, 1, 2, 7]]
    print(count(d))#48