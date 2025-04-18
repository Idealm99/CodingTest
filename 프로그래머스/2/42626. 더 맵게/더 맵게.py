import heapq
def solution(scoville, K):
    heap=[]
    for i in scoville :
        heapq.heappush(heap,i)
    count=0
    
    while len(heap) > 1 :
        one=heapq.heappop(heap)
        two=heapq.heappop(heap)
        if one >= K  :
            return count
        heapq.heappush(heap,one+(2*two))
        count+=1
        
    if max(heap) < K :
        return -1
    else :
        return count