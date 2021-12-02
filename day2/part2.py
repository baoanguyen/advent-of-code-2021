import os

def parse_line(input):
    direction = None
    distance = 0
    split_input = []
    
    direction, distance = input.split()
    
    return direction, int(distance)

def main():
    file = open("day2-data.txt", "r")

    inputs = {'horizontal': 0, 'depth': 0, 'aim': 0}

    direction = 0
    distance = 0

    data = file.readlines()
    
    
    for item in data:
        direction, distance = parse_line(item)
        print('aim = ', inputs['aim'], 'depth = ', inputs['depth'], 'horizontal = ', inputs['horizontal'])
        if direction == 'forward':
            inputs['horizontal'] += distance
            inputs['depth'] += (distance*inputs['aim'])
        elif direction == 'up':
            #inputs['depth'] -= distance
            inputs['aim'] -= distance
        elif direction == 'down':
            #inputs['depth'] += distance
            inputs['aim'] += distance

    print('depth = ', inputs['depth'], 'horizontal = ', inputs['horizontal'])
    print('aim = ', inputs['aim'])
    print(inputs['depth']*inputs['horizontal'])

main()