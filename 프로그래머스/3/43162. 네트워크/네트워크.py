def solution(n, computers):
    visited = [False] * n  # 각 컴퓨터 방문 여부

    def dfs(node):
        visited[node] = True
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                dfs(i)

    count = 0  # 네트워크 개수
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1  # 하나의 DFS 탐색이 하나의 네트워크를 의미

    return count
