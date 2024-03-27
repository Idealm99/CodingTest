def solution(arr1, arr2):
    a= len(arr1[0]) # 열
    b=len(arr2[0])
    li= []
    
    
    for i in  arr1:
        l=[]
        for idx in range(b):
            
            a=[ k[0]*k[1]  for k in zip(i, [j[idx] for j in arr2])]
            l.append(sum(a)) 
        li.append(l)
    return li
                    
                
                
            
        
    
    
# [[1, 4],  [[3, 3],
#  [3, 2],   [3, 3]]
#  [4, 1]]	