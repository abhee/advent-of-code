#!/usr/bin/env python3

import hashlib

def find_suffix(start, end, secret, n):
    pat = '0'*n
    for i in range(start, end):
        if hashlib.md5((secret+str(i)).encode('utf-8')).hexdigest()[0:n] == pat:
            # Return the very first suffix found
            return i               


if __name__ == '__main__':
    ## Part 1
    print(find_suffix(1, 10000000, 'yzbqklnj', 5))

    ## Part 2
    print(find_suffix(1, 10000000, 'yzbqklnj', 6))
