def solution(X, Y):

    dict_x={}
    dict_y={}
    re=''
    
    for i in X :
        if i in dict_x :
            dict_x[i]+=1
        else:
            dict_x[i]=1
    for i in Y :
        if i in dict_y :
            dict_y[i]+=1
        else:
            dict_y[i]=1  
            
    same=[]
    
    for i in dict_x.keys():
        if i in dict_y:
            same.append(i)
            
    if len(same) == 0:
        return "-1"
    elif len(same) == 1 and same ==['0']:
        return "0"
    
    else:
        same.sort(reverse=True)
        print(same)
        for i in same:
            re+=(i*min(dict_y[i],dict_x[i]))
            if re[0] =='0':
                re=re[1:]
            
        
        return re
        
