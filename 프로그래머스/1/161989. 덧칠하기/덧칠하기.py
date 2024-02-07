def solution(n, m, section):
    roller = section[0]
    cnt = 1
    for i in range(1, len(section)):
        if roller + m - 1 < section[i]:
            cnt += 1
            roller = section[i]
    return cnt


                

            
        
    
        
                    
    