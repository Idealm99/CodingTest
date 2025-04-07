from itertools import product

def solution(word):
    w = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    # 길이 1부터 5까지 조합 생성
    for i in range(1, 6):
        for p in product(w, repeat=i):
            words.append(''.join(p))
    
    # 사전순 정렬
    words.sort()
    
    # index + 1 (문제에 따라 1-based index일 수 있음)
    return words.index(word) + 1
