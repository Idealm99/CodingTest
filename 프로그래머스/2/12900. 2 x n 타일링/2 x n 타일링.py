MOD = 1000000007

def precompute_factorials(n, mod):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % mod
    
    inv_fact[n] = pow(fact[n], mod - 2, mod)  # Fermat's Little Theorem
    for i in range(n - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    
    return fact, inv_fact

def comb(n, k, fact, inv_fact, mod):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod

def solution(n):
    fact, inv_fact = precompute_factorials(n, MOD)
    count = 0
    for two in range(0, n // 2 + 1):
        one = n - 2 * two
        count = (count + comb(one + two, two, fact, inv_fact, MOD)) % MOD
    return count
