from itertools import product

def solution(numbers, target):
    i = ['+', '-']
    li=list(product(i, repeat=len(numbers))) 
    count=0
    
    for i in li :
        sum=0
        for j in range(len(numbers)) :
            if i[j] =='+':
                sum+=numbers[j]
            else: 
                sum-=numbers[j]
            
        
        if sum == target :
            count+=1
    return count
