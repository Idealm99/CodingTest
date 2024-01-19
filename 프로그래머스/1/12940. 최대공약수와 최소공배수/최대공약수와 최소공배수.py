def solution(n, m):
    li=[]
    mn, nn= max(n,m) , min(n,m)
    for i in range(nn+1,0,-1):
        if mn%i ==0 and nn%i==0:
            li.append(i)
            break
    for i in range(1,nn+1):
        if (i*mn)%nn == 0:
            li.append(i*mn)
            break
    
    return li

#     gcd = lambda a,b : b if not a%b else gcd(b, a%b)
#    lcm = lambda a,b : a*b//gcd(a,b)
#   return [gcd(n, m), lcm(n, m)]
