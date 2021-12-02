# Day 3 of Advent of Code 2015 - part 1

fhand = open('Dec3\input.txt')
directions = fhand.readline()
pos = [0,0] # x and y respectively
houses_dict = {(0,0):1}

for direction in directions:
    if direction == '>':
        pos[0] += 1
    if direction == '<':
        pos[0] -= 1
    if direction == '^':
        pos[1] += 1
    if direction == 'v':
        pos[1] -= 1
    if tuple(pos) not in houses_dict.keys():
        houses_dict[tuple(pos)] = 1
    else:
        houses_dict[tuple(pos)] += 1

print(f"Santa visited {len(houses_dict)} houses.")
