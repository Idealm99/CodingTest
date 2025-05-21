def solution(order):
    li=[i for i in range(len(order),0,-1)]
    
    sub =[]
    count=1
    
    for i in range(1,order[0]):
        sub.append(li.pop())
    
    li.pop()
    now =1
    flag=True
    
    while flag and now < len(order):
        if len(li) != 0 and order[now-1]<order[now] :
            while li:
                if li[-1] == order[now]:
                    li.pop()
                    break
                else:
                    sub.append(li.pop())
            now += 1
            count += 1

            # print(li,sub)
        else :
            if len(sub) != 0 and sub[-1] == order[now] :
                now+=1
                count+=1
                sub.pop()
                # print(li,sub)
            else :
                flag =False
    return count
                
