import collections

def solve(n,k):
    items = collections.deque()
    for i in range(1, n+1):
        items.append(i)
    
    for i in range(k):
        popped=items.popleft()
        items.append(items.popleft())
        items.append(popped)
    return items[0]

    

if __name__ == "__main__":
    print(solve(4, 3)) # 4
    print(solve(12, 5)) # 11
    print(solve(99, 555)) # 11
    print(solve(12345, 54321)) # 9875