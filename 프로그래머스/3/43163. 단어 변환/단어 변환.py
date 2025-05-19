from collections import deque



def solution(begin, target, words):
    if target not in words :
        return 0
    visit=set()
    que =deque()
    que.append((begin,0))
    
    while que :
        currrent, step = que.popleft()
        if currrent ==target :
            return step
        for word in words :
            count =0
            flag=True
            for a,b in zip(currrent,word) :
                if a != b :
                    count +=1
                if count > 1:
                    flag =False
                    break
            if word not in visit and flag :
                visit.add(word)
                que.append((word,step+1))
    
    return 0
                
                
            
            
    
    
