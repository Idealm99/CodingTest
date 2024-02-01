def gcd(n, limit, power):
    if n == 1:
        return 1

    count = 0
    for i in range(1, int(n ** 0.5) + 1):

        if n==i*i:
            count+=1
        elif n % i == 0:
            count += 2

    
    
    if count > limit: 
        return power
    else:
        return count
    
    

def solution(number, limit, power):
    li=[]
    for i in range(1,number+1):
        li.append(gcd(i,limit,power))
    
    return sum(li)