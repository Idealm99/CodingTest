def solution(num, total):
    if num==1:
        return[total]
    for i in range(-1000,total+1):
        sum=0
        for j in range(i,i+num):
            sum+=j
        
        if sum == total:
            return [k for k in range(i,i+num)]