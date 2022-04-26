# Day 5 of Advent of Code 2015 - part 2 WIP

def main():
   print(niceString())


def niceString():
    number_of_nice_strings = 0
    repeats = ''
    fhand = open('Dec5\input.txt')
    for line in fhand:
        is_repeating = False
        for letter in line:
            if len(repeats) == 3:
                if repeats[0] == repeats[2]:
                    is_repeating = True
                repeats = repeats[1:] + letter
            else:
                repeats += letter
        if is_repeating:
            number_of_nice_strings += 1
    return number_of_nice_strings


if __name__ == '__main__':
    main()
    