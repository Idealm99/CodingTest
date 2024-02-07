def solution(dartResult):
    sum=0
    nums=['1','2','3','4','5','6','7','8','9','0']
    sig={'S':'**1','D':'**2','T':'**3'}
    op={'*':'*2','#':'*-1'}
    li=[]
    k=[]
    for i in dartResult:
        if i in op:
            li[-1].append(i)
            continue
        
        k.append(i)
        if i in sig: 
            li.append(k)
            k=[] 
            
    for idx,i in enumerate(li) :
        if i[0] == '1' and i[1] == '0' :
            li[idx][0]+=li[idx].pop(1)
    print(li)
    st=''
    for idx, word in enumerate(li) :
        for  i in word :
            if i in sig :
                st+=sig[i]
            elif i in op :
                st+=op[i]
            else:
                st=st+'+'+i
        if idx+1<len(li) and li[idx+1][-1] =='*':
             st+=op['*']
    return eval(st[1:])
        
        
            
        
        
        
            
            