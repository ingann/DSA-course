
def find(t, k): 
    if len(t) == 1:
        return max(t[0]-1, k-t[0])
    if len(t) == 2:
        t.sort()
        biggest = t[-1]-t[0]
        first = t[0]-1
        last = k-t[-1]

        if first >= biggest//2 or last >= biggest//2:
            if first < last:
                return last
            return first

        return biggest//2

    l = sorted(t)
    tsorted = []
    dic = {}

    for n in l:
        if n not in dic:
            tsorted.append(n)
            dic[n] = n

    print(tsorted)

    biggest = max_diff(tsorted)
    first= tsorted[0]-1
    last = k-tsorted[-1]

    if first >= biggest//2 or last >= biggest//2:
        if first < last:
            return last
        return first

    return biggest//2

def max_diff(numbers):
    n = len(numbers)
    result = numbers[1] - numbers[0]
    for i in range(2, n):
        result = max(result, numbers[i] - numbers[i - 1])
    
    return result


if __name__ == "__main__":
    print(find([1, 2, 9], 11), "\n") # 3
    print(find([2, 1, 3], 3), "\n") # 0
    print(find([7, 4, 10, 4], 10), "\n") # 3
    print(find([15, 2, 6, 4, 18], 20), "\n") # 4
    print(find([41222388, 392676742, 307110407, 775934683, 25076911], 809136843),"\n") # 191628970
    print(find([7, 12, 4], 15), "\n") #3
    print(find([2, 11, 9, 10, 10], 15), "\n")#4