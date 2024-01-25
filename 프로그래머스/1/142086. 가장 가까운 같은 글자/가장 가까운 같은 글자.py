def solution(s):
    dick = {}
    for idx, ap in enumerate(s):
        if ap in dick.keys():
            dick[ap].append(idx)
        else:
            dick[ap] = [idx]
    print(dick)
    li =[None]*len(s)
    key = list(dick.keys()) 
    print(key)
    for i in key:
        value = list(dick[i])
        for idx, j in enumerate(value) :
            if idx == 0 :
                li[j]= -1
            else:
                li[j]=value[idx]-value[idx-1]
    return li