import re

file = open('input', 'r')
data = file.readlines()


def part_one(lines):
    sum_part_numbers = 0
    for line in lines:
        for match in re.finditer(r'\d+', line):
            start = 0 if match.start() - 1 < 0 else match.start() - 1
            if re.search('[^.\n\d]\d+|\d+[^.\n\d]', line[start:match.end()+1]):
                sum_part_numbers += int(line[match.start():match.end()])
                continue
            if lines.index(line)+1 < len(lines):
                next_line = lines[lines.index(line)+1]
                if re.search('[^.\n\d]', next_line[start:match.end()+1]):
                    sum_part_numbers += int(line[match.start():match.end()])
                    continue
            if lines.index(line)-1 >= 0:
                prev_line = lines[lines.index(line)-1]
                if re.search('[^.\n\d]', prev_line[start:match.end()+1]):
                    sum_part_numbers += int(line[match.start():match.end()])
    return sum_part_numbers


data = [
"12.......*.."
"+.........34",
".......-12..",
"..78........",
"..*....60...",
"78.........9",
".5.....23..$",
"8...90*12...",
"............",
"2.2......12.",
".*.........*",
"1.1..503+.56"
]

def part_two(lines):
    gears = {}
    sum_gear_ratios = 0
    for line in lines:
        for match in re.finditer(r'\d+', line):
            start = 0 if match.start() - 1 < 0 else match.start() - 1
            if re.search('^\*(\d+)|(\d+)\*$', line[start:match.end() + 1]):
                s = line[start:match.end() + 1]
                i = start + s.index("*")

                # sum_part_numbers += int(line[match.start():match.end()])
                continue
            if lines.index(line) + 1 < len(lines):
                next_line = lines[lines.index(line) + 1]
                if re.search('[^.\n\d]', next_line[start:match.end() + 1]):
                    sum_gear_ratios += int(line[match.start():match.end()])
                    continue
            if lines.index(line) - 1 >= 0:
                prev_line = lines[lines.index(line) - 1]
                if re.search('[^.\n\d]', prev_line[start:match.end() + 1]):
                    sum_gear_ratios += int(line[match.start():match.end()])
    return sum_gear_ratios

# Part one
#print(part_one(data))

print(part_two(data))