from collections import deque

def solution(queue1, queue2):
    # 조기 종료 조건들
    total = sum(queue1) + sum(queue2)
    if total % 2 != 0:  # 홀수면 절반으로 나눌 수 없음
        return -1
    
    target = total // 2
    q1s = sum(queue1)
    
    if q1s == target:  # 이미 같으면 0 반환
        return 0
    
    # 덱 생성
    q1 = deque(queue1)
    q2 = deque(queue2)
    q2s = total - q1s
    
    count = 0
    max_operations = 3 * (len(queue1) + len(queue2))  # 더 합리적인 상한
    
    while q1 and q2 and count < max_operations:
        if q1s == target:
            return count
            
        if q1s > target:
            # q1에서 q2로 이동
            val = q1.popleft()
            q2.append(val)
            q1s -= val
            count += 1
        else:
            # q2에서 q1로 이동
            val = q2.popleft()
            q1.append(val)
            q1s += val
            count += 1
    
    return -1