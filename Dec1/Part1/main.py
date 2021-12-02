# Day 1 of Advent of Code 2015 - part 1

floor = 0
fhand = open('Dec1\input.txt')
file = fhand.readline()
for i in file:
    if i == '(':
        floor += 1
    else:
        floor -= 1
print(f"Final floor is {floor}")
