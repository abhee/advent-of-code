#!/usr/bin/env python3

# Part 1
with open("input.txt") as f:
    print(sum([1 if i=='(' else -1 for i in f.readline()]))

# Part 2
with open("input.txt") as f:
    cur_pos = 0
    chars_read = 0

    for char in f.readline():
        chars_read += 1
        if char == '(':
            cur_pos += 1
        else:
            cur_pos -= 1
            if cur_pos == -1:
                print(chars_read)
                break
