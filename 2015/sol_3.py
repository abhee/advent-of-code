def read_input():
    with open("inputs/input_3.txt") as f:
        return f.read().strip()

def houses_visited(directions):
    houses = set()

    # Assuming that santa's starting location is 0,0
    x, y = 0, 0
    houses.add((x,y))

    for d in directions:
        if d == '>':
            x += 1
        elif d == '<':
            x -= 1
        elif d == '^':
            y += 1
        elif d == 'v':
            y -= 1
        else:
            pass

        houses.add((x,y))

    return houses


if __name__ == '__main__':
    directions = read_input()
    
    ## Part 1
    print(len(houses_visited(directions)))

    ## Part 2
    santas_directions = directions[0::2]
    robo_directions = directions[1::2]

    print(len(houses_visited(santas_directions).union(houses_visited(robo_directions))))