def solution(strings, n):
    #a.sort(key=i[n])으로도 정렬이 됨
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
    
