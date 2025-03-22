def solution(priorities, location):
    queue = [(p, i) for i, p in enumerate(priorities)]  # (우선순위, 원래 인덱스)
    
    count = 0

    while queue:
        cur = queue.pop(0)
        
        if any(cur[0] < q[0] for q in queue):  # 뒤에 더 높은 우선순위가 있다면
            queue.append(cur)
        else:  # 출력됨
            count += 1
            if cur[1] == location:
                return count
