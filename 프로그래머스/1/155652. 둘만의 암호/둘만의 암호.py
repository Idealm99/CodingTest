def solution(s, skip, index):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for a in range(len(skip)):
        alpha.remove(skip[a])
    
    
        
    st=''
    for i in s:
        st += alpha[(alpha.index(i)+index)%len(alpha)]
    return st


        
        
    

            

