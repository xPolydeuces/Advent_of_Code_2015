# Day 5 of Advent of Code 2015 - part 1

def main():
   print(niceString())


def niceString():
    number_of_nice_strings = 0
    vowels = ('a','e','i','o','u')
    forbidden_strings = ('ab','cd','pq','xy')
    fhand = open('Dec5\input.txt')
    for line in fhand:
        vowel_count = 0
        previous_letter = ''
        is_twice_in_a_row = False
        is_not_forbidden = True
        for letter in line:
            if letter in vowels:
                vowel_count += 1
            if previous_letter == letter:
                is_twice_in_a_row = True
            if previous_letter + letter in forbidden_strings:
                is_not_forbidden = False
            previous_letter = letter
        if vowel_count >= 3 and is_twice_in_a_row and is_not_forbidden:
            number_of_nice_strings += 1
    return number_of_nice_strings


if __name__ == '__main__':
    main()
    