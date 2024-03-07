import math

def solution(n):
    count = 0
    a = n // 2
    for i in range(0, a + 1):
        count += math.comb(n - i , i)
        print(math.comb(n - i * 2, i), n-2*i,i)
    return count%1234567

# def jumpCase(num):
#     a, b = 1, 2
#     for i in range(2,num):
#         a, b = b, a+b
#     return b

# #아래는 테스트로 출력해 보기 위한 코드입니다.
# print(jumpCase(4))
        
    
    
    