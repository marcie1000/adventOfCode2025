#!/usr/bin/env python3

def puzzle(lines, removeRolls: bool, removedCount: int = 0):
    maxX = len(lines[0]) - 1
    maxY = len(lines)

    total = 0

    removables = []

    for posY in range(maxY):
        for posX in range(maxX):

            if lines[posY][posX] == '.':
                continue

            adjRolls = 0

            for lookY in range(-1, +2):
                if lookY + posY < 0 or lookY + posY >= maxY: continue
                for lookX in range(-1, +2):
                    if lookX + posX < 0 or lookX + posX >= maxX or (lookX == 0 and lookY == 0): continue
                    if lines[posY + lookY][posX + lookX] == '@':
                        adjRolls += 1

            if adjRolls < 4:
                total += 1
                removables.append((posX, posY))

    if removeRolls:
        for aRoll in removables:
            lines[ aRoll[1] ] = lines[ aRoll[1] ][:aRoll[0]] + '.' + lines[ aRoll[1] ][aRoll[0] + 1:]
            removedCount += 1

    return total, lines, removedCount

if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        lines = f.readlines()

    total, _, _ = puzzle(lines, False)
    print("Part 1:", total)

    end = False
    removedCount = 0

    while not end:
        total, lines, removedCount = puzzle(lines, True, removedCount=removedCount)
        if total == 0:
            end = True

    print("Part 2:", removedCount)
