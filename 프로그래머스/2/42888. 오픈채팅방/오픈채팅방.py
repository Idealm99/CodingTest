def solution(record):
    dt={}
    count=0
    result=[]
    for i in record :
        w = i.split(' ')
        if w[0]=='Enter':
            user_id, name=w[1],w[2]  
            dt[user_id]= name
        else :
            if  w[0] == 'Change':
                dt[w[1]]=w[2]
                
    for i in record :
        w = i.split(' ')
        if w[0]=='Enter':
            result.append(f'{dt[w[1]]}님이 들어왔습니다.')
        elif w[0]=='Leave': 
            result.append(f'{dt[w[1]]}님이 나갔습니다.')
    return result