def solution(N, road, K):
    import heapq
    INF = float('inf')
    
    # 1. 그래프(인접 리스트) 초기화
    graph = [[] for _ in range(N + 1)]
    for a, b, n in road:
        graph[a].append((n,b)) # (도착 노드, 비용)
        graph[b].append((n,a)) # 양방향 도로
    
    # 2. 최단 거리 배열 초기화
    # distance[i]는 1번 마을에서 i번 마을까지의 최단 거리를 저장
    distance = [INF] * (N + 1)
    
    # 3. 우선순위 큐(Min-Heap) 초기화: (비용, 노드)
    q = []
    distance[1] = 0
    heapq.heappush(q, (0, 1)) # (비용 0, 시작 노드 1)
    
    # 4. 다익스트라 메인 루프
    while q:

        cost , node = heapq.heappop(q)
        
        if distance[node] < cost : 
            continue
        
        for next_cost,next_node in graph[node] :
            new_cost = cost+next_cost
            if new_cost < distance[next_node] :
                distance[next_node]=new_cost
                heapq.heappush(q,(new_cost,next_node))
                
                
    # 5. K 이하인 마을의 개수 세기
    answer = 0
    for dist in distance[1:]:
        if dist <= K:
            answer += 1
            
    return answer