def solution(lottos, win_nums):
    count=0
    zero=0
    no =0
    for i in lottos :
        if i == 0 :
            zero+=1
        elif i in win_nums :
            count +=1

    
    # 최고 순위 zero + count 
    # 최저 순위 count 개수
    li = [zero+count,count]
    re=[]
    
    
    for i in li :
        if i <=1 :
            re.append(6)
        else:
            re.append(7-i)
    return re
        
    
    
    