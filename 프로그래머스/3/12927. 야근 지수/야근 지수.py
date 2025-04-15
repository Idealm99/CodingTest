import heapq as hq
def solution(n, works):
    heap=[]
    for i in works:  
        hq.heappush(heap,-i)
    for _ in range(n):
        ma=hq.heappop(heap)
        if ma == 0 :
            return 0
        
        hq.heappush(heap,ma+1)
    sum=0    
    for i in heap :
        sum+=(i*i)
    return sum
    