def solution(n):
    f=[0,1]
    i=0

    while i <=n-2 :
        f.append(f[i]+f[i+1])
        i+=1

    return f[-1]%1234567
    
