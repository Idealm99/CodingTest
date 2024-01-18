

def solution(name, yearning, photo):
    sum=[]
    
    for i in photo :
        psum=0
        for j in range(len(name)):
            psum += i.count(name[j])*yearning[j]
        sum.append(psum)
            
            
        
    
    return sum