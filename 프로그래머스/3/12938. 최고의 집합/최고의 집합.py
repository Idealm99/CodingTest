def solution(n, s):
    if s < n:
        return [-1]  # 1 이상 자연수이므로

    a = s // n
    r = s % n
    print(r)
    # r개의 a+1, 나머지는 a
    answer = [a + 1] * r + [a] * (n - r)

    return sorted(answer)
