#!/usr/bin/env python3

dial = 50
counterP1 = 0
counterP2 = 0

def rotation(line):
    global dial, counterP1, counterP2

    n = int(line[1:])

    counterP2 += n // 100
    prev = dial

    if line[0] == "L":
        dial = dial - (n % 100)
    else:
        dial = dial + (n % 100)

    if dial < 0:
        if prev != 0:
            counterP2 += 1
        dial = 100 + dial
    elif dial > 99:
        dial = dial - 100
        counterP2 += 1
    elif dial == 0 and (n % 100) != 0:
        counterP2 += 1

    if dial == 0:
        counterP1 += 1

if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        lines = f.readlines()

    for line in lines:
        rotation(line)

    print("Part 1:", counterP1)
    print("Part 2:", counterP2)
