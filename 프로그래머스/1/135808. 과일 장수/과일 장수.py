def solution(k, m, score):
    a= sorted(score, reverse = True)
    sum=0
    for i in range( len(score)//m):
        sum+=min(a[i*m:(i+1)*m])*m
        
    return sum   
        
    
    
        