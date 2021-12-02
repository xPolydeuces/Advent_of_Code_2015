# Day 4 of Advent of Code 2015 - part 1
import hashlib
number = 0
for i in range(0,999999):
    key_input = "iwrupvqb"
    number += 1
    key_input = key_input + str(number)
    result = hashlib.md5(key_input.encode()).hexdigest()
    if result.startswith("00000"):
        print(number)
        break