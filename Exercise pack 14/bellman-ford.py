import random
import time

class BellmanFord:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.edges = []
        
    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))

    def find_distances(self, start_node):
        random.shuffle(self.edges)
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0
        
        for _ in range(len(self.nodes) - 1):
            for edge in self.edges:
                node_a, node_b, weight = edge
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    
        return distances
    

if __name__ == "__main__":
    n = 5000
    alg = BellmanFord(n)
    print("n:", n)
    
    for node in range(1, 4992):
        for i in range(node+1, node+10):
            alg.add_edge(node, i, random.randint(1, 1000))

    start_time = time.time()
    result = alg.find_distances(1)
    end_time = time.time()

    print("result:", result)
    print("time:", round(end_time - start_time, 2), "s")
