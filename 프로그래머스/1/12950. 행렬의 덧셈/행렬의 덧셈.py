
def solution(arr1, arr2):
    ad=[]
    
    for row1, row2 in zip(arr1,arr2):
        
        ad.append([row1[i]+row2[i] for i in range(len(row1))])
        

    return   ad      
        
        
    
    
    