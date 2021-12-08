import os

def parse_line(input):
    direction = None
    distance = 0
    split_input = []
    
    direction, distance = input.split()
    
    return direction, int(distance)

def main():
    file = open("day3-data.txt", "r")

    data = file.readlines()
    
    
    gamma_rate = []

    ones = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    zeroes = [0,0,0,0,0,0,0,0,0,0,0,0]
    

    for line in data:
        line.strip()
        
        for index, char in enumerate(line):
            
            #print(line)
            if char == '1':
                ones[index] += 1
            if char == '0':
                zeroes[index] += 1

   
    # Find Gamma    
    for index, char in enumerate(ones):
        if ones[index] > zeroes[index]:
            gamma_rate.append(1)
        else:
            gamma_rate.append(0)
    #gamma_rate_dec = int("".join(str(x) for x in gamma_rate))
    gamma_rate_dec = 0
    epsilon_rate_dec = 0
    # Epsilon
    epsilon_rate = []
    for item in gamma_rate:
        epsilon_rate.append(item^1)
    
    for bit in gamma_rate:
        gamma_rate_dec = (gamma_rate_dec << 1) | bit
    
    for bit in epsilon_rate:
        epsilon_rate_dec = (epsilon_rate_dec << 1) | bit
    
    ans = gamma_rate_dec*epsilon_rate_dec
    print(gamma_rate)
    print(epsilon_rate)
    print('\n', gamma_rate_dec)
    print(epsilon_rate_dec)
    print(ans)
main()
