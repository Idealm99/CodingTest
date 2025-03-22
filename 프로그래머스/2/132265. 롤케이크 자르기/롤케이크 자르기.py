from collections import defaultdict

def solution(topping):
    answer = 0
    left = set()
    right_count = defaultdict(int)

    # 처음에 오른쪽에 모든 토핑 개수 기록
    for t in topping:
        right_count[t] += 1

    for i in range(len(topping) - 1):
        t = topping[i]
        
        # 왼쪽에 추가
        left.add(t)
        
        # 오른쪽에서 하나 빼기
        right_count[t] -= 1
        if right_count[t] == 0:
            del right_count[t]

        # 왼쪽과 오른쪽의 서로 다른 토핑 수 비교
        if len(left) == len(right_count):
            answer += 1

    return answer
