def solution(n, t, m, p):
    def convert(num, base):
        digits = "0123456789ABCDEF"
        if num == 0:
            return "0"
        res = ''
        while num > 0:
            res = digits[num % base] + res
            num //= base
        return res

    sequence = ''
    i = 0
    while len(sequence) < t * m:
        sequence += convert(i, n)
        i += 1

    result = ''
    for i in range(t):
        result += sequence[i * m + (p - 1)]
    
    return result
