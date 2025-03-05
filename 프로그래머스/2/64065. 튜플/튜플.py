def solution(s):
    s= s[1:-1]+',}'

    a=[]
    ln=[]
    st=''
    for i in s :
        if i == '{':
            a=[]
            
        elif i == '}' :
            ln.append(a)
            
                
        elif i == ',' :
            a.append(int(st))
            st=''
        else:
            st+=i
            
    
   
    c=[0]*(len(ln)-1)
    for i in ln :
        c[len(i)-1]=i
        
    answer=[]
    dick={}
    for i in c :
        for j in i:
            if j not in answer :
                answer.append(j)
    
    return answer