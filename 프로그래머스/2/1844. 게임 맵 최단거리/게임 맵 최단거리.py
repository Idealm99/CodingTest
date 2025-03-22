from collections import deque

def solution(maps):
    n, m = len(maps) , len(maps[0])
    que =deque() 
    que.append((0,0))# 현재 위치
    
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    
    while que :
        loc = que.popleft()
        for i in range(4):
            
            row=loc[0] + dx[i]
            columns=loc[1] +dy[i]
            if 0<=row < n and 0<=columns <m and maps[row][columns] ==1 :
                maps[row][columns] = maps[loc[0]][loc[1]]+1
                que.append((row,columns))
        
    if maps[n-1][m-1] == 1:
        return -1  # 도달하지 못함
    else:
        return maps[n-1][m-1]            
    