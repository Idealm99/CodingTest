def solution(n, a, b):
    if a > n / 2 and b > n / 2:
        return solution(n / 2, a - n / 2, b - n / 2)
    elif a <= n / 2 and b <= n / 2:
        return solution(n / 2, a, b)
    else:
        c = 0
        while n > 1:
            n = n // 2
            c += 1
        return c
# 배울만한 코드   
# def solution(n,a,b):
#     answer = 0
#     while a != b:
#         answer += 1
#         a, b = (a+1)//2, (b+1)//2

#     return answer
