
from collections import deque
def solution(queue1, queue2):

    count=0
    q1=deque(queue1)
    q2=deque(queue2)
    q1s=sum(queue1)
    q2s=sum(queue2)
    target= (q1s+q2s)/2
    print(target,q1s,q2s)
    while q1 and q2 and 4^(len(queue1)+len(queue2))>count:
        if q1s > q2s :
            q2.append(q1.popleft())
            q2s+=q2[-1]
            q1s-=q2[-1]
            count+=1
        elif q1s < q2s:
            q1.append(q2.popleft())
            q2s-=q1[-1]
            q1s+=q1[-1]
            count+=1

        else:
            
            return count

    return -1
            
# 10 5 1
# 2 2 2
# 5 1 / 2 2 2 10  . 5 1 2 / 2 2 10 . 5 1 2 2 / 2 10   . 5 1 2 2 2 / 10
