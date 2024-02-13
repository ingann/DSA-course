def count(x):
    result = x
    for c1 in range(5):
        for c4 in range(5):
            rest = x - c1 - c4 * 4
            if rest >= 0 and rest % 5 == 0:
                result = min(result, c1 + c4 + rest // 5)
    return result

if __name__ == "__main__":
    print(count(8)) # 2
    print(count(6)) #2
    print(count(13)) #3
    print(count(12345)) # 2469
    print(count(1337**9)) # 2730314408854633746890878156