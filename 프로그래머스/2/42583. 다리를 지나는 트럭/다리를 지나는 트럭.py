from collections import deque 
def solution(bridge_length, weight, truck_weights):
    count=0
    time=deque()
    
    truck_weights=deque(truck_weights)
    ing=deque()
    ing.append(truck_weights.popleft())
    time.append(count+bridge_length)
    # print(sum(ing))
    while truck_weights or ing :
        count+=1
        if count >=time[0] :
                time.popleft()
                ing.popleft()
        s=sum(ing)
        if  truck_weights and s+truck_weights[0]  <= weight :
            ing.append(truck_weights.popleft())
            time.append(count+bridge_length)
            
        
            
        
            
            
        
    return count+1