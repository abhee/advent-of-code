#!/usr/bin/env python3

## Part 1
def paper_per_box(l, w, h):
    s1 = l*w
    s2 = w*h
    s3 = h*l
    return 2*(s1+s2+s3) + min(s1,s2,s3)

## Part 2
def ribbon_per_box(l, w, h):
    # smallest side
    s1 = min(l,w,h)

    # second smallest side
    if s1 == l:
        s2 = min(w,h)
    elif s1 == w:
        s2 = min(l,h)
    else:
        s2 = min(l,w)
    
    return (l*w*h) + 2*(s1+s2)


if __name__ == '__main__':
    total_paper = 0
    total_ribbon = 0
    
    with open("input.txt") as f:
        for line in f.readlines():
            l,w,h = (int(i) for i in line.strip().split('x'))
            total_paper += paper_per_box(l, w, h)
            total_ribbon += ribbon_per_box(l,w,h)

    
    print(total_paper)
    print(total_ribbon)
        
            
