
def solution(arr1, arr2):
    li=[]
    ad=[]
    count=0
    for row1, row2 in zip(arr1,arr2):
        for r1,r2 in zip(row1,row2):
            ad.append(r1+r2)
            count+=1
        

        if count == len(arr1[0]):
            count=0
            li+=[ad]
            ad=[]
    return   li      
        
        
    
    
    