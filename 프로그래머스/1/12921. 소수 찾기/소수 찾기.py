def a(n):
    count=0
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1
def solution(n):
    count=0
    for i in range(2,n+1):
        count+=a(i)
    return count