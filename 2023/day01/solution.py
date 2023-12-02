def get_calibration_value_p1(line):
    first = 0
    last = 0
    for e in line:
        if e.isnumeric():
            last = e
            if not first:
                first = e
    return first + last


def check_ints(line):
    first = len(line) - 1
    last = 0
    for i, e in enumerate(line):
        if e.isnumeric():
            last = i
            if i < first:
                first = i
    return {"first": first, "last": last}


def get_calibration_value_p2(line):
    fl_indexes = check_ints(line)
    first_index = fl_indexes["first"]
    last_index = fl_indexes["last"]
    first = line[first_index]
    last = line[last_index]
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for d in digits:
        if line.find(d) != -1:
            if line.find(d) < first_index:
                first_index = line.find(d)
                first = digits.index(d) + 1
            if line.rfind(d) > last_index:
                last_index = line.rfind(d)
                last = digits.index(d) + 1
    return str(first) + str(last)


file = open('input', 'r')
lines = file.readlines()
sum_part_one = 0
sum_part_two = 0

for l in lines:
    sum_part_one += int(get_calibration_value_p1(l))
    sum_part_two += int(get_calibration_value_p2(l))

# Part 1
print(f'Sum calibration value part 1: {sum_part_one}')

# Part 2
print(f'Sum calibration value part 2: {sum_part_two}')