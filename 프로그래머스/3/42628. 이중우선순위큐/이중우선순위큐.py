import heapq

def solution(operations):
    heap = []
    
    for i in operations:
        command, n = i.split()
        n = int(n)

        if command == 'I':
            heapq.heappush(heap, n)
        elif command == 'D' and heap:
            if n == 1:
                # 최대값 삭제 (heap에서 최대값 제거)
                heap.remove(max(heap))
                heapq.heapify(heap)  # 다시 힙 구조 유지
            elif n == -1:
                # 최소값 삭제 (heapq는 기본적으로 최소힙)
                heapq.heappop(heap)

    if heap:
        return [max(heap), min(heap)]
    else:
        return [0, 0]
