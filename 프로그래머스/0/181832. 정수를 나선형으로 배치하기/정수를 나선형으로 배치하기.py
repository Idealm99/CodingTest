def solution(n):
    dx = [1, 0, -1, 0]  # 우, 하, 좌, 상
    dy = [0, 1, 0, -1]
    
    # 올바르게 2차원 리스트 초기화
    li = [[0] * n for _ in range(n)]
    
    x, y = 0, 0
    direct = 0
    
    for i in range(1, n * n + 1):
        li[y][x] = i
        nx = x + dx[direct]
        ny = y + dy[direct]
        
        # 경계 조건 및 이미 방문한 경우 방향 전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n or li[ny][nx] != 0:
            direct = (direct + 1) % 4
            nx = x + dx[direct]
            ny = y + dy[direct]
        
        x, y = nx, ny
    
    return li
