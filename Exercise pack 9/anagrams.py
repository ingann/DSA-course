import itertools
def create(s):
    result = {}

    for permutation in itertools.permutations(s):
        if permutation not in result:
            result[''.join(permutation)] = 0
    return sorted(result)

if __name__ == "__main__":
    print(create("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create("aaaaa")) # ['aaaaa']
    print(create("abab")) # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    print(len(create("aybabtu"))) # 1260