def solution(babbling):
    words=[ "aya", "ye", "woo", "ma"]
    
    count =0
    
    for i in babbling :
        li=''
        last=''
        for j in i:
            li+=j
            if len(li) <= 3 and li in  words and li != last:
                last=li
                li=''
                
            
        if li =='':
            count +=1
    return count