def solution(genres, plays):
    diction={}
    gl=list(set(genres))
    for i in range(len(genres)):
        if genres[i] in diction :
            
            diction[genres[i]]['s']+=plays[i]
            diction[genres[i]]['n'].append([plays[i],i])
        else:
            diction[genres[i]]={'s':plays[i], 'n':[[plays[i],i]]} 
    
    result=[]
    gl.sort(key = lambda x : diction[x]['s'],reverse=True)
    for i in gl :
        data =diction[i]['n']
        data.sort(key=lambda x: (-x[0],x[1]))
        print(data)
        count=0
        
        while count < len(data) and count < 2 :
        
            result.append(data[count][1])
            count+=1
            
    return result
