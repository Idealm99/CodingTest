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

