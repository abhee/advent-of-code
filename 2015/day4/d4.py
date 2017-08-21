import hashlib

def find_suffix(start, end, secret, pat):
    for i in range(start, end):
        if hashlib.md5((secret+str(i)).encode('utf-8')).hexdigest()[0:5] == pat:
            # Return the first suffix found
            if i > 0:
                return i               
            

if __name__ == '__main__':
    ## Part 1
    print(find_suffix(1, 10000000, 'yzbqklnj', '00000'))

    ## Part 2
    print(find_suffix(1, 10000000, 'yzbqklnj', '000000'))
    
