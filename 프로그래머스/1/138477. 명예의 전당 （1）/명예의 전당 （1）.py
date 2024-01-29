def solution(k, score):
    re=[]
    p=[]
    for i in score:
        if len(p) ==k :
            if p[0] < i:
                p[0]=i
                p.sort()
            re.append(p[0])
        else:
            p.append(i)
            p.sort()
            re.append(p[0])
            
    return re