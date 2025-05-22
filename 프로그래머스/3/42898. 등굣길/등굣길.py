def solution(m, n, puddles):
    grid = [[0]*m for _ in range(n)]
    for i in puddles:
        
        grid[i[1]-1][i[0]-1] = -1
        
    grid[0][0]=1
    MOD = 10**9+7
    for x in range(m):
        for y in range(n):
            if grid[y][x] != -1 : 
                if y+1 <=n-1 and grid[y+1][x] != -1:
                    grid[y+1][x]+=grid[y][x]
                if x+1 <=m-1 and grid[y][x+1] != -1:
                    grid[y][x+1]+=grid[y][x]
    return grid[n-1][m-1] % MOD

def solution(m, n, puddles):
    MOD = 10**9+7
    # 1) puddle 좌표를 0-based set 으로
    blocked = {(x-1, y-1) for x, y in puddles}

    # 2) 1차원 DP: 열 방향으로만 관리
    dp = [0] * m
    dp[0] = 1  # 출발점

    for y in range(n):
        for x in range(m):
            if (x, y) in blocked:
                dp[x] = 0
            else:
                # 왼쪽에서 넘어오는 경우만 더하기
                if x > 0:
                    dp[x] = (dp[x] + dp[x-1]) 

    return dp[-1]% MOD
