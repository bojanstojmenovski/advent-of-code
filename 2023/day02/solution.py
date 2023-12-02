import re

def is_game_possible(game):
    subset_colors = re.split(", |; ", game)
    for subset_color in subset_colors:
        color_data = subset_color.split(" ")
        if int(color_data[0]) > colors[color_data[1]]:
            return False
    return True


def get_game_sets_power(game):
    colors_min = {"red": 1, "green": 1, "blue": 1}
    subset_colors = re.split(", |; ", game)
    p = 1
    for subset_color in subset_colors:
        color_data = subset_color.split(" ")
        if int(color_data[0]) > colors_min[color_data[1]]:
            colors_min[color_data[1]] = int(color_data[0])
    for n in colors_min.values():
        p *= n
    return p


file = open('input', 'r')
lines = file.readlines()
colors = {"red": 12, "green": 13, "blue": 14}
sum_ids_possible_games = 0
sum_power_sets = 0

for line in lines:
    line = line.replace("\n", "")
    line_data = line.split(": ")
    game_data = line_data[1]
    sum_power_sets += get_game_sets_power(game_data)
    if is_game_possible(game_data):
        game_id = int(line_data[0].split(" ")[1])
        sum_ids_possible_games += game_id

# Part 1
print(f'Sum of IDs of possible games: {sum_ids_possible_games}')

# Part 2
print(f'Sum of power for each game set: {sum_power_sets}')
