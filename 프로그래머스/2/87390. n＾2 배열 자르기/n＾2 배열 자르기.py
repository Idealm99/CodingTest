def solution(n, left, right):
    a=left // n +1
    aa=left % n # a 번째 주기의 시작 인덱스
    b= right//n+1
    bb=right%n # b번째 주기의 마지막 인덱스
    
    li=[a]*a + [i for i in range(a+1,n+1)]
    if a==b :
        return li[aa:bb+1]
    
    li=li[aa:]
        
    
    

    
    # left가 몇번째인지(aa) 그리고 몇번째 주기인지(a)
    # right도 같음
    for i in range(a+1,b):
        li+=[i]*i+[j for j in range(i+1,n+1)]
    
    ll=[b]*b + [i for i in range(b+1,n+1)]
    li+=ll[:bb+1]
    
    return li
                
                