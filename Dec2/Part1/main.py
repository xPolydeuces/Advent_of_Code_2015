# Day 2 of Advent of Code 2015 - part 1

fhand = open('Dec2\input.txt')
result = 0
paper = lambda l, w, h: 2*l*w + 2*w*h + 2*h*l
for line in fhand:
    line = line.split('x')
    smallest_side = sorted([int(line[0])*int(line[1]), int(line[1])*int(line[2]), int(line[2])*int(line[0])])
    result += paper(int(line[0]), int(line[1]), int(line[2])) + smallest_side[0]
print(f"Total square feet of paper needed are {result}")
