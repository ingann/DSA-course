import heapq
def calculate(t):
    graph = {node: [] for node in range(0, len(t))}
    graph = add_edges(t, graph)
    graph = Dijkstra(graph)
    result = graph.find_distances(0)
    return result

def add_edges(t, graph):

    idx = 0
    for node in t:
        if idx + node < len(t):
            graph[idx].append((idx+node, t[idx]))
        if idx-node >= 0:
            graph[idx].append((idx-node, t[idx]))
        idx += 1


    return graph

class Dijkstra:
    def __init__(self, graph):
        n = len(graph)
        self.nodes = range(n)
        self.graph = graph
        
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
                    
        if distances[len(self.graph)-1] == float("inf"):
            return -1
        return distances[len(self.graph)-1]
    
if __name__ == "__main__":
    print(calculate([1, 1, 1, 1])) # 3
    print(calculate([3, 2, 1])) # -1
    print(calculate([3, 5, 2, 2, 2, 3, 5])) # 10
    print(calculate([7, 5, 3, 1, 4, 2, 4, 6, 1])) # 32