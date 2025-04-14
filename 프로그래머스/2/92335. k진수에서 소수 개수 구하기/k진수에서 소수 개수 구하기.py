def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True
def solution(n, k):
    a = ''
    while n > k:
        a = str(n % k) + a
        n //= k
    a = str(n) + a

    count = 0
    for i in a.split('0'):
        if i and is_prime(int(i)):
            count += 1
    return count
