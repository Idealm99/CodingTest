


def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            # 같은 열(j)은 제외하고 이전 행(i-1)에서 최댓값을 더해준다
            land[i][j] += max(land[i-1][k] for k in range(4) if k != j)
    
    return max(land[-1])
