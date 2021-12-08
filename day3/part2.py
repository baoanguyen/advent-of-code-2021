import os

def parse_line(input):
    direction = None
    distance = 0
    split_input = []
    
    direction, distance = input.split()
    
    return direction, int(distance)

def main():
    file = open("day3-test.txt", "r")

    data = file.readlines()
        
    rmListOxygen = []
    rmListCarbon = []

    common = []
    ones = [0,0,0,0,0]
    zeroes = [0,0,0,0,0]
    rmCount = 11
    # ones = [0,0,0,0,0,0,0,0,0,0,0,0]
    # zeroes = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    for line in data:
        line.strip()
        for index, char in enumerate(line):
            #print(line)
            if char == '1':
                ones[index] += 1
            elif char == '0':
                zeroes[index] += 1
    
    oxygen = data.copy()
    carbon = data.copy()
    
    # Find Common    
    for index, char in enumerate(ones):
        if ones[index] >= zeroes[index]:
            common.append(1)
        else:
            common.append(0)
    # Find Least Common
    uncommon = []
    for index, char in enumerate(ones):
        if ones[index] > zeroes[index]:
            uncommon.append(1)
        else:
            uncommon.append(0)
    print(ones)
    print(zeroes)
    print(common)
    # Oxygen Rating
    
    for item in oxygen:
        item.strip()
        
        if len(rmListOxygen) >= rmCount:
                break
        for index, char in enumerate(common):
            
            if len(rmListOxygen) >= rmCount:
                break
                #char=int  item[index]=str
                
            if str(char) != item[index]:
                print('removed: ', item,'comparison: ', item[index], '\t', char)
                rmListOxygen.append(item)
                break

    for item in rmListOxygen:
        oxygen.remove(item)

    
    for item in carbon:
        item.strip()
        if len(rmListCarbon) >= rmCount:
                break
        for index, char in enumerate(uncommon):
            if len(rmListCarbon) >= rmCount:
                break
            elif char != item[index]:
                rmListCarbon.append(item)
                break
  
    for item in rmListCarbon:
        carbon.remove(item)

    oxygen_dec, carbon_dec = 0, 0

    print(oxygen)
    print(int(oxygen[0], 2))
    print(int(carbon[0], 2))
    ans = int(carbon[0], 2)*int(oxygen[0], 2)
    print(ans)
main()
