#!/usr/bin/env python3

def read_input():
    with open("inputs/input_1.txt", "r") as f:
        return f.read().strip()

instructions = read_input()

# Part 1
def which_floor(inp):
    '''Returns floor number Santa would be on after following the instructions'''
    return sum([1 if char =='(' else -1 for char in inp])

print(which_floor(instructions))


# Part 2
def char_to_basement(inp):
    '''Returns first character that leads Santa to the basement for first time'''
    cur_pos = 0

    for index, char in enumerate(inp):

        cur_pos += (1 if char == '(' else -1)

        if cur_pos == -1:
            return index + 1

print(char_to_basement(instructions))