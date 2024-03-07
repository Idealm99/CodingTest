def solution(n):
    li=[ i for i in range(1,3*n+1) if i%3 != 0 and '3' not in str(i)]
    return li[n-1]