def solution(arr):
    li =[]
    for i in arr :
        if len(li) >0 :
            if li[-1] != i :
                li.append(i)
        else:
            li.append(i)
            
    return li