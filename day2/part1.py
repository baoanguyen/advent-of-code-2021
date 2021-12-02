import os

def parse_line(input):
    direction = None
    distance = 0
    split_input = []
    
    direction, distance = input.split()
    
    return direction, int(distance)

def main():
    file = open("day2-data.txt", "r")

    inputs = {'horizontal': 0, 'depth': 0}

    direction = 0
    distance = 0

    data = file.readlines()
    
    
    for item in data:
        direction, distance = parse_line(item)
        
        if direction == 'forward':
            inputs['horizontal'] += distance
            
        elif direction == 'up':
            inputs['depth'] -= distance
        elif direction == 'down':
            inputs['depth'] += distance


    
    print(inputs['depth']*inputs['horizontal'])

main()
