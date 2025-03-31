def solution(dirs):
    now = [0, 0]
    visited = set()
    dt = {'U': [1, 0], 'D': [-1, 0], 'R': [0, 1], 'L': [0, -1]}

    for d in dirs:
        move = dt[d]
        next_x = now[0] + move[0]
        next_y = now[1] + move[1]

        # 범위 체크
        if not (-5 <= next_x <= 5 and -5 <= next_y <= 5):
            continue

        # 경로를 정렬된 형태로 저장하여 중복 제거
        path = (
            (min(now[0], next_x), min(now[1], next_y)),
            (max(now[0], next_x), max(now[1], next_y))
        )

        visited.add(path)
        now = [next_x, next_y]

    return len(visited)
