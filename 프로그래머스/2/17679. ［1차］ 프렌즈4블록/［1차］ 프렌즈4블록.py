def solution(m, n, board):
    # 문자열을 리스트로 변환 (수정 가능하게)
    board = [list(row) for row in board]
    
    total_removed = 0
    
    while True:
        # 제거할 블록들의 좌표를 저장할 집합
        to_remove = set()
        
        # 2x2 블록 찾기
        for y in range(m-1):
            for x in range(n-1):
                if (board[y][x] != '-' and 
                    board[y][x] == board[y+1][x] == board[y][x+1] == board[y+1][x+1]):
                    # 2x2 블록의 모든 좌표 추가
                    to_remove.add((y, x))
                    to_remove.add((y+1, x))
                    to_remove.add((y, x+1))
                    to_remove.add((y+1, x+1))
        
        # 제거할 블록이 없으면 종료
        if not to_remove:
            break
            
        # 블록 제거
        for y, x in to_remove:
            board[y][x] = '-'
        
        # 제거된 블록 수 누적
        total_removed += len(to_remove)
        
        # 중력 적용 (각 열마다)
        for x in range(n):
            # 현재 열에서 '-'가 아닌 문자들만 수집
            column = []
            for y in range(m):
                if board[y][x] != '-':
                    column.append(board[y][x])
            
            # 열을 다시 채우기 (위쪽은 '-', 아래쪽은 블록)
            for y in range(m):
                if y < m - len(column):
                    board[y][x] = '-'
                else:
                    board[y][x] = column[y - (m - len(column))]
    
    return total_removed