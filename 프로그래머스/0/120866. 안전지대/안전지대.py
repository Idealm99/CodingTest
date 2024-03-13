def switch(board,idxx,idxy):
    li=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for i in li :
        try:
            if board[idxy+i[0]][idxx+i[1]] !=1 and idxy+i[0] >=0 and idxx+i[1]>=0:
                board[idxy+i[0]][idxx+i[1]] =2
            pass
        except :
            pass
            
    return board   
        
        
    
def solution(board):
    count=0
    for idxy, n in enumerate(board):
        for idxx,i in enumerate(n) :
            if i == 1 :
                board=switch(board,idxx,idxy)
                
    
    for i in board:
        count+=i.count(0)
    print(board)
    return count   