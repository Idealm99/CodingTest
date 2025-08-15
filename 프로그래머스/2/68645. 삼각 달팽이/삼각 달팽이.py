import math
def solution(n):
    anwer = [[0]*i for i in range(1,n+1)]
    direct=[(0,1),(1,0),(-1,-1)]
    nsum=0
    for i in range(1,n+1):
        nsum+=i
    count=2
    now=[0,0]
    anwer[0][0]=1
    d=0

    while count <= nsum :
        d=d%3
        y=now[1]+direct[d][1]
        x=now[0]+direct[d][0]
        if 0<=x<n and 0<=y<n and anwer[y][x] == 0 :
            anwer[y][x] = count 
            now=[x,y]
            count+=1
        else :
            d+=1
            continue
    result=[]
    for i in anwer :
        result.extend(i)
    return result