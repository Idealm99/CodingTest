def solution(strings, n):
    dict={}
    for i in strings :
        if i[n] in dict :
            dict[i[n]].append(i)
        else: 
            dict[i[n]]=[i]
    a=sorted(dict.keys())
    result=[]
    for i in a:
        result+=sorted(dict[i])
    
    return result
    
