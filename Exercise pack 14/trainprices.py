import heapq

class TrainPrices:
    def __init__(self):
        self.graph = {}

    def add_city(self, name):
        self.graph[name] = []

    def add_train(self, city1, city2, price):
        if city2 not in self.graph[city1]:
            self.graph[city1].append((city2, price))
        if city1 not in self.graph[city2]:
            self.graph[city2].append((city1, price))

    def find_prices(self):
        result = [[]]
        result[0] = [None]
        result[0] += sorted(self.graph)

        for city in sorted(self.graph):
            result.append(self.prices(city))
    
        return result


    def prices(self, start_node):

        distances = {}
        for node in self.graph:
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

        for node in distances:
            if distances[node] == float("inf"):
                distances[node] = -1
    
        distances = sorted(distances.items())
        result = [start_node]
        for key, value in distances:
            result.append(value)
        return result


if __name__ == "__main__":
    t = TrainPrices()

    t.add_city("Helsinki")
    t.add_city("Turku")
    t.add_city("Tampere")
    t.add_city("Oulu")

    t.add_train("Helsinki", "Tampere", 20)
    t.add_train("Helsinki", "Turku", 10)
    t.add_train("Tampere", "Turku", 50)

    print(t.find_prices())

    # metodin haluttu tulos:
    # [[None,       'Helsinki', 'Oulu', 'Tampere', 'Turku'],
    #  ['Helsinki', 0,          -1,     20,        10],
    #  ['Oulu',     -1,         0,      -1,        -1],
    #  ['Tampere',  20,         -1,     0,         30],
    #  ['Turku',    10,         -1,     30,        0]]