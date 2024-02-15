def solution(keymap, targets):
    dict={}
    for i in keymap:
        for idx,a in enumerate(i):
            if a in dict :
                dict[a]= min(dict[a],idx+1)
            else:
                dict[a]=idx+1
    print(dict)
    re=[]
    for i in targets :
        sum=0
        for j in i:
            if j in dict:
                sum+=dict[j]
            else:
                sum= -1
                break
        re.append(sum)
    return re