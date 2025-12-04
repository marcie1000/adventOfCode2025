#!/usr/bin/env python3

def puzzle(lines, ranks: int):
    total = 0

    for l in lines:

        rankNumbers = [0] * ranks
        rankPos = [0] * ranks

        rankPos[-1] = -1

        for iRank in range(ranks):
            iPos = rankPos[iRank - 1] + 1
            for char in l[rankPos[iRank - 1] + 1 : - (ranks - iRank)]:
                number = int(char)
                if number > rankNumbers[iRank]:
                    rankNumbers[iRank] = number
                    rankPos[iRank] = iPos
                iPos += 1

        total += int("".join(str(i) for i in rankNumbers))

    return total

if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        lines = f.readlines()

    print(f"Part 1: {puzzle(lines, 2)}")
    print(f"Part 2: {puzzle(lines, 12)}")
