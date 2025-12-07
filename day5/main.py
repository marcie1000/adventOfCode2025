#!/usr/bin/env python3
class RRange:
    def __init__(self):
        self.mmin = 0
        self.mmax = 0

ranges = []

def parse(lines):
    global ranges

    i = 0
    end = False
    while not end:

        if lines[i] == "\n":
            end = True
        else:
            pos = lines[i].find('-')
            r = RRange()
            r.mmin = int(lines[i][:pos])
            r.mmax = int(lines[i][pos + 1:])
            ranges.append(r)

        i += 1

    return ranges, i

def part1(lines, start):

    global ranges

    total = 0
    for n in range(start, len(lines)):
        ingredient = int(lines[n])
        for aRange in ranges:
            if aRange.mmin <= ingredient <= aRange.mmax:
                total += 1
                break

    print("Part 1:", total)

def simplifyRanges():

    global ranges
    # simplify by finding duplicates

    newRanges = ranges.copy()

    # 1st case :
    # AAA-AAA
    #          BBB-BBB
    # result: no changes
    #
    # 2nd case :
    # AAA-------AAA
    #     BBB--------BBB
    # Result:
    # AAA------------AAA
    #
    # 3rd case :
    #     AAA----AAA
    # BBB------------BBB
    # Result:
    # AAA------------AAA
    #
    # 4th case :
    # AAA------------AAA
    #     BBB----BBB
    # Result:
    # AAA------------AAA
    #
    # 5th case:
    #      AAA-------AAA
    # BBB-------BBB
    # Result :
    # AAA------------AAA
    #
    # 6th case:
    #          AAA-AAA
    # BBB-BBB
    # result: no changes


    iA = 0

    while iA < len(newRanges):

        rangeA = newRanges[iA]
        iB = iA + 1
        while iB < len(newRanges):
            incrementB = False

            rangeB = newRanges[iB]

            # case 1 - case 6
            if iA == iB or rangeA.mmax < rangeB.mmin or rangeB.mmax < rangeA.mmin:
                incrementB = True

            # case 2
            elif rangeA.mmin <= rangeB.mmin <= rangeA.mmax <= rangeB.mmax:
                rangeA.mmax = rangeB.mmax
                newRanges.pop(iB)


            # case 3
            elif rangeB.mmin <= rangeA.mmin <= rangeA.mmax <= rangeB.mmax:
                rangeA.mmin = rangeB.mmin
                rangeA.mmax = rangeB.mmax
                newRanges.pop(iB)


            # case 4
            elif rangeA.mmin <= rangeB.mmin <= rangeB.mmax <= rangeA.mmax:
                newRanges.pop(iB)


            # case 5
            elif rangeB.mmin <= rangeA.mmin <= rangeB.mmax <= rangeA.mmax:
                rangeA.mmin = rangeB.mmin
                newRanges.pop(iB)


            if incrementB:
                iB += 1
        iA += 1

    ranges = newRanges
            
def part2():
    total = 0
    for r in ranges:
        total += r.mmax - r.mmin + 1
    print("Part 2:", total)

if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        lines = f.readlines()

    ranges, start = parse(lines)

    part1(lines, start)

    oldRangeLen = 0

    while oldRangeLen != len(ranges):
        oldRangeLen = len(ranges)
        simplifyRanges()

    part2()
