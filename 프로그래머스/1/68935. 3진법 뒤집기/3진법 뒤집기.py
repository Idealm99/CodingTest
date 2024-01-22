def solution(n): 
    a=[]
    while n >= 3 :
        a.append( n%3)
        n= n//3
    a.append(n) 
    sum=0
    for i in a:
        sum+=i
        sum*=3
    return sum/3    
    
#     def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3
#     answer = int(tmp, 3)
#     return answer
