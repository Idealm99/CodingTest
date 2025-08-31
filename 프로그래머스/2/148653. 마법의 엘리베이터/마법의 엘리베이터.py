# 엘리베이터가 위치해 있는 층과 버튼의 값을 더한 결과가 0보다 작으면 엘리베이터는 움직이지 않습니다
# 현재 층 더하기 |10^n|
# 0층이 가장 아래
# 1버튼 = 1 마법의돌
# 0층으로 가야한다 
# 35이면 

def solution(storey):
    answer = 0
    li=[]
    while storey >= 1 :
        
        li.append(storey % 10)
        storey = storey//10
        # 4 , 5, 5, 2
    count=0
    next =0
    for i in range(len(li)-1) :
        li[i]+=next
        if li[i] < 5 :
            count+=li[i]
            next=0
        elif li[i] ==5 and li[i+1] <=4:
            count+=li[i]
            next=0
        else :
            count+=(10-li[i])
            next=1
    li[-1]+=next
    # print(count,li[-1])
    if li[-1] < 6 :
        count+=li[-1]
    else:
        count+=(11-li[-1])
            
    return count