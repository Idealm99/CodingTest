def solution(n):
    
    re=0
    while n >= 1:
        if n%2 == 0 :
            n /=2
        else: 
            n-=1
            re+=1
        
    
    return re