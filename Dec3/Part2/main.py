# Day 3 of Advent of Code 2015 - part 2

fhand = open('Dec3\input.txt')
directions = fhand.readline()
pos_santa = [0,0] # x and y respectively
pos_robo_santa = [0,0]
houses_dict = {(0,0):1}

def move(pos: list, active = True):
    for direction in directions:
        if active:
            active = False
            continue
        else:
            active = True
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

move(pos_santa)
move(pos_robo_santa, False)

print(f"Santa visited {len(houses_dict)} houses.")
