import os
import re

os.chdir("/Users/bojanstojmenovski/Desktop/advent-of-code/2023/day06")


file = open('input', 'r')
lines = file.readlines()

ts = re.split("\s+", re.split(": ", lines[0])[1].strip())
distances = re.split("\s+", re.split(": ", lines[1])[1].strip())

def get_possible_wins(time, distance):
    mmpms = 1
    w = 0
    for mmpms in range(time):
        if (time - mmpms) * mmpms > distance:
            w += 1
        mmpms += 1
    return w


part_one = 1
for time in ts:
    i = ts.index(time)
    part_one *= get_possible_wins(int(ts[i]), int(distances[i]))


# Part one
print(f'Part one: {part_one}')

# Part two
print(f'Part two: {get_possible_wins(int("".join(ts)), int("".join(distances)))}')