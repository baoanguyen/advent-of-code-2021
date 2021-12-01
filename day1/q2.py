import os


def countSums(arr:list):
    prev_item1 = 0
    prev_item2 = 0
    sum_arr = []
    
    for item in arr:
        
        #Exception Handling at the start
        if(prev_item2 == 0):
            prev_item2 = item
            continue
        elif(prev_item1 == 0):
            prev_item1 = item
            continue
        else:
            sum_arr.append(prev_item1+prev_item2+item)
            
            prev_item2 = prev_item1
            prev_item1 = item
    return sum_arr

def main():

    ans = 0
    prev_item = 0

    file = open("day1-data.txt", "r")
    List = file.readlines()
    int_List = [int(item) for item in List]
    Sums = countSums(int_List)

    
    for item in Sums:
        
        if prev_item < item:
            ans +=1
        
        prev_item = item
    ans -= 1
    print('Sums = ', len(Sums))
    print('Answer = ', ans)
    
    return (ans)
main()
    


