import os

answer = 0

def main():

    ans = 0
    prev_item = 0

    file = open("day1-data.txt", "r")
    List = file.readlines()
    

    for item in List:
        
        if prev_item < int(item):
            ans +=1
        
        prev_item = int(item)
    return (ans-1)

answer = main()
print(answer)