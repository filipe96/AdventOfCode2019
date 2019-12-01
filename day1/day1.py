import math

def getData():
    with open("input1.txt") as f:
            data = f.read().split("\n")
    return data

def calc(mass):
    return math.floor(mass / 3)  - 2


def main():
    sum = 0
    for mass in getData():
        sum += calc(int(mass))
    
    print(sum)

main()