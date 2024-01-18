def solution(n, lost, reserve):
    new_lost=[]
    for i in lost :
        if i in reserve :
            reserve.remove(i)
        else:
            new_lost.append(i)
    print(new_lost,reserve)
    new_lost.sort()
    reserve.sort()
    if len(new_lost) == 0:
        return n
    for i,num in enumerate(new_lost) :
        if num-1 in reserve:
            new_lost[i]=-1
            reserve.remove(num-1)
        elif num+1 in reserve :
            new_lost[i]=-1
            reserve.remove(num+1)
    print(new_lost,reserve)
    count=0
    for i in new_lost :
        if i != -1 :
            count+=1
    return n-count
        