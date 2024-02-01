def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

            
            
def solution(nums):
    from itertools import combinations
    re=0

    at=list(combinations(nums,3))
    a=[]

    for i in at :
        a.append(sum(i))
    

    for i in a :
        if is_prime(i):
            re+=1
        
                 

    return re