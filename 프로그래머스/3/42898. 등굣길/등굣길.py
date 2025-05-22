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