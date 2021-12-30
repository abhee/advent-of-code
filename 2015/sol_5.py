#!/usr/bin/env python3


### Part 1

def has_three_vowels(s):
    ''' Returns True if string has atleast 3 distinct vowels. '''
    vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

    for i in s:
        if i in vowels:
            vowels[i] += 1

    return sum(vowels.values()) >= 3

def has_a_double_letter(s):
    ''' Returns True if string has atleast one letter that appears twice in a row. '''
    
    for i in range(len(s)):
        if s[i:i+2] == s[i]*2:
            return True

    return False

def contains_invalid_string(s):
    ''' Returns True if string contains strings "ab", "cd", "pq" or "xy" '''
    
    for i in ["ab", "cd", "pq", "xy"]:
        if i in s:
            return True

    return False
            
def is_nice_1(s):
    ''' Determines if supplied string is nice or naughty '''
    
    s = s.lower() 

    return has_three_vowels(s) and has_a_double_letter(s) and not contains_invalid_string(s)

## Tests
assert is_nice_1('ugknbfddgicrmopn') == True
assert is_nice_1('aaa') == True
assert is_nice_1('jchzalrnumimnmhp') == False
assert is_nice_1('haegwjzuvuyypxyu') == False
assert is_nice_1('dvszwmarrgswjxmb') == False


### Part 2

def has_repeat_pair(s):
    ''' pair of any two letters that appears at least twice in the string without overlapping '''
    
    pairs_seen = set()

    for idx in range(len(s)):
        ## Non overlapping repeat pair having same letter - ex. aaaa
        if s[idx : idx+2] == s[idx+2 : idx+4]:
            return True

        ## Overlapping repeat pair having same letter - ex. aaa
        if s[idx : idx+2] == s[idx+1 : idx+3]:
            return False

        if s[idx : idx+2] in pairs_seen:
            return True
        
        pairs_seen.add(s[idx : idx+2])

    return False


def has_palindromic_triple(s):
    ''' Returns True if string contains one letter which repeats with exactly one letter between the 
        two occurrences
    '''
    
    for idx in range(len(s)):
        if idx < len(s)-2 and s[idx] == s[idx+2]:
            return True

    return False


def is_nice_2(s):
    ''' Determines if supplied string is nice or naughty '''
    
    s = s.strip().lower()

    return has_repeat_pair(s) and has_palindromic_triple(s)
 
## Tests
assert is_nice_2('qjhvhtzxzqqjkmpb') == True
assert is_nice_2('xxyxx') == True
assert is_nice_2('aaa') == False
assert is_nice_2('aaaa') == True
assert is_nice_2('uurcxstgmygtbstg') == False
assert is_nice_2('ieodomkazucvgmuy') == False


#### Print answer

with open('inputs/input_5.txt') as f:
    inp = f.readlines()
    print(sum([is_nice_1(eachLine) for eachLine in inp]))
    print(sum([is_nice_2(eachLine) for eachLine in inp]))
