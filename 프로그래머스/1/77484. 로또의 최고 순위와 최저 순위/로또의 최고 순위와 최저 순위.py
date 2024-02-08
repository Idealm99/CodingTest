def solution(lottos, win_nums):
    count=0
    zero=0
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
        
#     인덱스로 푼 경우    
#         rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]

    
    