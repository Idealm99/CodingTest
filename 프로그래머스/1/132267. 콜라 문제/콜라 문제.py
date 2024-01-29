# 먼저 // 를 이용해서 몇개 만들어지는지 구하고 나머지가 있는지 확인하고 있으면 나중에 부족할 때 사용하고 
def solution(a, b, n):
    cnt=0
    rest=0
    while n >= a :
        k=n
        n= ((n)//a)*b
        rest= k%a
        cnt += n
        n += rest
        
    
    
    return cnt
    
    