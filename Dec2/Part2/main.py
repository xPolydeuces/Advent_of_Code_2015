# Day 2 of Advent of Code 2015 - part 2

fhand = open('Dec2\input.txt')
result = 0
ribbon = lambda l, w, h: 2*l + 2*w + l*w*h
for line in fhand:
    line = line.split('x')
    line = sorted([int(line[0]), int(line[1]), int(line[2])])
    result += ribbon(int(line[0]), int(line[1]), int(line[2]))
print(f"Total feet of ribbon needed is {result}")
