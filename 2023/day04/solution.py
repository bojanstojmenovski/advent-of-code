import re

file = open('input', 'r')
scratchcards = file.readlines()

def get_card_points(win_numbers, numbers):
    points = 0
    x = 0
    for n in win_numbers:
        if n in numbers:
            points = 2**x
            x += 1
    return points


def part_one(cards):
    total_points = 0
    for card in cards:
        card = card.replace("\n", "")
        card_data = re.split(" \| ", re.split(": ", card)[1])
        wn = re.split("\s{1,2}", card_data[0])
        n = re.split("\s{1,2}", card_data[1])
        total_points += get_card_points(wn, n)
    return total_points


# Part one
#print(f'Part one (total points): {part_one(scratchcards)}')


def get_card_n_matching_numbers(win_numbers, numbers):
    matching_numbers = 0
    for n in win_numbers:
        if n in numbers:
            matching_numbers += 1
    return matching_numbers


def get_card_number(card):
    return re.search(r"\d+", re.split(": ", card)[0]).group()


def part_two(cards):
    total_scratchcards = 0
    notes = {}
    q = 1
    while q <= len(cards):
        notes[str(q)] = 1
        q += 1
    for card in cards:
        card = card.replace("\n", "")
        card_number = get_card_number(card)
        card_data = re.split(" \| ", re.split(": ", card)[1])
        wn = re.split("\s{1,2}", card_data[0])
        n = re.split("\s{1,2}", card_data[1])
        matching = get_card_n_matching_numbers(wn, n)
        i = 1
        while i <= matching and i < len(cards):
            notes[str(int(card_number) + i)] += notes[card_number]
            i += 1
    for x in notes.values():
        total_scratchcards += x
    return total_scratchcards


# Part two
print(f'Part two (total scratchcards): {part_two(scratchcards)}')