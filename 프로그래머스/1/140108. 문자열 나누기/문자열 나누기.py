def solution(s):
    a=0
    b=0
    re=0

    st=''
    f=''
    for idx,i in enumerate(s) :
        if  f =='':
            
            f= i
        if i==f :
            a+=1
        else :
            b+=1
        
        if a==b:
            a=0
            b=0
            re+=1
            f=''
    if f!='':
        re+=1
    return re
            
            