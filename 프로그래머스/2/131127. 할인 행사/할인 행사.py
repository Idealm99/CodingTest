def solution(want, number, discount):
    s=sum(number)
    count=0
    for i in range(len(discount)-s+1):
        flag=True
        
        for idx,w in enumerate(want): 
            if flag==True and discount[i:i+s].count(w) ==number[idx]:
                falg=True
            else: 
                flag=False
                break
        if flag == True:
            count+=1
    return count