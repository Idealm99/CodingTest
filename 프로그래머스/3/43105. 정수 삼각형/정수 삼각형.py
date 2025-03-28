def solution(triangle):
    memory = [[0]*len(triangle[i]) for i in range(len(triangle))]
    memory[0][0]=triangle[0][0]
    dx =[0,1]
    for y in range(len(triangle)-1):
        for x in range(len(triangle[y])):
            sum=memory[y][x]
            
            for i in dx :
                if sum+triangle[y+1][x+i] > memory[y+1][x+i] :
                    memory[y+1][x+i] = sum+triangle[y+1][x+i]
    return max(memory[-1])