import heapq

def smallest(n):
    heap = [1]

    for i in range(n):
        heapq.heappush(heap, heap[0]*2)
        heapq.heappush(heap, heap[0]*3)
        heapq.heappop(heap)
    return heap[0]

if __name__ == "__main__":
    print(smallest(1)) # 2
    print(smallest(5)) # 6
    print(smallest(123)) # 288
    print(smallest(55555)) # 663552