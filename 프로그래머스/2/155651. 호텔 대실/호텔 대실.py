# 목표 : 최소한의 객실 사용 
# 퇴실 후 10간 청소 후 객실 사용 가능
from collections import deque 
def solution(book_time):
    time=[]
    if len(book_time) ==1 :
        return 1
    for start,end in book_time :
        s=start.split(':')
        e=end.split(':')
        time.append([int(s[0])*60+int(s[1]),int(e[0])*60+int(e[1])+10])
    # print(sorted(time))
    
    time=deque(sorted(time))
    count=0
    # print(time)
    que=[time.popleft()]
    while time :
        now=[]
        start , end = time.popleft()
        for s, e in que :
            if e > start :
                now.append([s,e])
        now.append([start,end])
        que=now
        count=max(count,len(now))
        
            
        
        
    
    return count