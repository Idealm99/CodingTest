def solution(N, stages): # n 층에 실패한 사람/ n층에 도전한 사람 
    sum_ch=[]
    for i in range (1,N+1):
        count=0
        for j in stages :
            if j >= i :
                count+=1
        sum_ch.append(count)
    
    fail=[]
    for i in range(N):
        fail.append(stages.count(i+1))
    print(fail, sum_ch)
    for i in range(len(sum_ch)):
        if fail[i]==0:
            sum_ch[i]=0
        else:
            sum_ch[i] =fail[i]/sum_ch[i]
    
    
           
            
    sorted_idx = sorted(range(N), key=lambda x: sum_ch[x],reverse = True)
    for i in range(len(sorted_idx)):
        sorted_idx[i]+=1
    return sorted_idx
