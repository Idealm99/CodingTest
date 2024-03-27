def solution(arr1, arr2):
    
    b=len(arr2[0])
    li= []
    
    
    
    li=[[ sum(k[0]*k[1]  for k in zip(i, [j[idx] for j in arr2])) for idx in range(b)]for i in  arr1]
            
        
    return li
                    
                
                
            
        
    
    
# [[1, 4],  [[3, 3],
#  [3, 2],   [3, 3]]
#  [4, 1]]	