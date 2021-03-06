#!/usr/bin/env python3

def has_three_vowels(s):
    """ Returns True if string has atleast 3 distinct vowels."""
    vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

    for i in s:
        if i in vowels.keys():
            vowels[i] += 1

    return sum(vowels.values()) >= 3

def has_a_double_letter(s):
    """ Returns True if string has atleast one letter that appears twice in a row."""
    
    double_found = False
    
    for i in range(len(s)):
        if s[i:i+2] == s[i]*2:
            double_found = True
            break

    return double_found

def contains_invalid_string(s):
    '''Returns True if string contains strings "ab", "cd", "pq" or "xy"'''
    
    flag = False
    
    for i in ["ab", "cd", "pq", "xy"]:
        if i in s:
            flag = True
            break

    return flag
            
def is_nice(s):
    """ Determines if supplied string is nice or naughty"""
    
    s = s.lower() 

    return has_three_vowels(s) and has_a_double_letter(s) and not contains_invalid_string(s)


if __name__ == '__main__':
    with open('input.txt') as f:
        print(sum([is_nice(eachLine) for eachLine in f.readlines()]))
