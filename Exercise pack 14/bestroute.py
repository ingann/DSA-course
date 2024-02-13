import heapq
class BestRoute:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.graph = {node: [] for node in range(1, n + 1)}

    def add_road(self, a, b, x):
        if b not in self.graph[a]:
            self.graph[a].append((b, x))
        if a not in self.graph[b]:
            self.graph[b].append((a, x))

    def find_route(self, a, b):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[a] = 0
        
        queue = []
        heapq.heappush(queue, (0, a))
        
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
                    
        if distances[b] == float("inf"):
            return -1
        
        return distances[b]
                


if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1, 2, 2)
    print(b.find_route(1, 3)) # -1
    b.add_road(1, 3, 5)
    print(b.find_route(1, 3)) # 5
    b.add_road(2, 3, 1)
    print(b.find_route(1, 3)) # 3
    print()
    b = BestRoute(5)
    print(b.find_route(3,4))
    b.add_road(3,5,7)
    print(b.find_route(3,4))
    print(b.find_route(1,4))
    b.add_road(3,4,6)
    print(b.find_route(4,5))
    b.add_road(4,5,4)
    b.add_road(1,2,7)
    b.add_road(1,3,4)
    print(b.find_route(3,4))