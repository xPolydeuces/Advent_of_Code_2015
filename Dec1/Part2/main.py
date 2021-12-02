# Day 1 of Advent of Code 2015 - part 2

floor, pos = 0, None
fhand = open('Dec1\input.txt')
line = fhand.readline()
for idx, val in enumerate(line):
    if val == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        pos = idx + 1
        break
print(f"Position at which Santa enters basement is {pos}")
