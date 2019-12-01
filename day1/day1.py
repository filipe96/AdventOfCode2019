import math

def getData():
    with open("input1.txt") as f:
            data = f.read().split("\n")
    return data

def calc(mass):
    return math.floor(mass / 3)  - 2

def recurisiveFuleCalc(fuel):
    if calc(fuel) <= 0:
        return 0 
    else: 
        return calc(fuel) + recurisiveFuleCalc(calc(fuel))

def main():
    sum = 0
    for mass in getData():
        sum += recurisiveFuleCalc(int(mass))
    print(sum)
    print(recurisiveFuleCalc(sum))

main()