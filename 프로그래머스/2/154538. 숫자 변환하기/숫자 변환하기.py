from collections import deque

def solution(x: int, y: int, n: int) -> int:
    # BFS 큐에 (현재값, 연산횟수) 저장
    queue = deque([(y, 0)])
    visited = {y}

    while queue:
        cur, cnt = queue.popleft()
        if cur == x:
            return cnt

        # 2로 나누기
        if cur % 2 == 0:
            nxt = cur // 2
            if nxt >= x and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, cnt + 1))

        # 3으로 나누기
        if cur % 3 == 0:
            nxt = cur // 3
            if nxt >= x and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, cnt + 1))

        # n 빼기
        nxt = cur - n
        if nxt >= x and nxt not in visited:
            visited.add(nxt)
            queue.append((nxt, cnt + 1))

    return -1




