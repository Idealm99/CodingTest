def solution(n, wires): 
    from collections import deque
    connect=[[] for _ in range(n+1)]
    for a, b in wires :
        connect[a].append(b)
        connect[b].append(a)
        
    
    result=n
    
    for a , b in wires :
        que= deque([a])
        visit = set()
        
        count=0
        
        while que :
            now=que.pop()
            for i in connect[now] :
                if i != b and i not in visit :
                    que.append(i)
            # que.extend(connect[now])
            if now != b and   now not in visit:
                count +=1
                visit.add(now)
        result=min(result,abs(n-count*2))
    
    return result
        
                
            
            
            

            ## 미리 연결된 지점을 알고 있다
    
    
    
    
#     min_val=n
#     for i in range(len(wires)):
#         li1=set()
#         li2=set()
#         li1.add(wires[i][0])
#         li2.add(wires[i][1])
#         last=[]
#         for j in range(len(wires)):
#             if i!=j:
#                 if wires[j][0] in li1 or wires[j][1] in li1:
#                     li1.add(wires[j][0])
#                     li1.add(wires[j][1])
#                 elif wires[j][0] in li2 or wires[j][1] in li2:
#                     li2.add(wires[j][0])
#                     li2.add(wires[j][1])
#                 else :
#                     last.append(wires[j])
#         while last:
#             temp=last.pop(0)
#             if temp[0] in li1 or temp[1] in li1:
#                 li1.add(temp[0])
#                 li1.add(temp[1])
#             elif temp[0] in li2 or temp[1] in li2:
#                 li2.add(temp[0])
#                 li2.add(temp[1])
#             else :
#                 last.append(temp)
#         val=abs(len(set(li1))-len(set(li2)))
#         min_val = min(min_val,val)
        
#     return min_val