from itertools import permutations

def sosu(n):
    if n < 2:  # 1은 소수가 아님
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def solution(numbers):
    nlist = [str(i) for i in numbers]  # 문자열로 변환
    visit = set()
    count = 0
    
    # 1개부터 전체 길이까지의 순열 생성
    for i in range(1, len(nlist) + 1):
        perms = list(permutations(nlist, i))
        
        for perm in perms:
            num_str = ''.join(perm)
            num = int(num_str)
            
            # 중복 제거 및 소수 판별
            if num not in visit:
                visit.add(num)
                if sosu(num):
                    count += 1
    
    return count