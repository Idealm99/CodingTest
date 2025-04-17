def solution(msg):
    dict={}
    result=[]
    for i in range(65,91) :
        dict[chr(i)]=i-64
    dict['']=0
    result=[]
    now=''
    count=27
    for i in msg :
        
        if now + i in dict :
            now=now+i
            
        else: 
            result.append(dict[now])        
            dict[now+i]=count
            now=i
            count+=1
    result.append(dict[now])
    return result 