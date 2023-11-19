#The robot starts moving from square (0, 0). After that the robot moves according to the given motion series one step at a time. The motion series consists of up, down, left and right. The goal is to count in how many different squares the robot visits.
#Time complexity for this algorithm is O(n)
#A function returns the count of different squares 

def count(s):
    locations = set()
    locations.add(Location(0, 0))
    ver = 0 #vertical
    hor = 0 #horizontal

    dic = {"L": -1, "D": -1, "R": 1, "U": 1}

    for dir in s:
        if dir == "R" or dir == "L":
            ver += dic[dir]
        else:
            hor += dic[dir]
        locations.add(Location(hor, ver))
    return len(locations)

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


if __name__ == "__main__":
    print(count("LL")) # 3
    print(count("UUDLRR")) # 5
    print(count("UDUDUDU")) # 2
