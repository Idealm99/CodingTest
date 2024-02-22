def solution(board, moves):
    stack=[0]
    re=0
    for idx in moves :
        for i, j in enumerate(board) :
            if j[idx-1] != 0:
                if j[idx-1] == stack[-1]:
                    stack.pop()
                    board[i][idx-1]=0
                    re+=2
                    break
                else:
                    stack.append(j[idx-1])
                    board[i][idx-1]=0   
                    break
                    
                
    return re