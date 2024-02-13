import collections
import time
import random

def test_add(n):
    items = collections.deque()

    for i in range(1, n+1):
        items.append(i)

def test_remove(n):
    items = collections.deque([*range(1, n+1)])

    for i in range(n):
        items.popleft()

    
if __name__ == "__main__":
    n = 10**5
    print("n:", n)
    random.seed(1337)

    start_time = time.time()
    #result = test_add(n)
    result = test_remove(n)
    end_time = time.time()

    print("result:", result)
    print("time:", round(end_time - start_time, 2), "s")