
def solution(n):

    answer = [[0] * i for i in range(1, n + 1)]
    
    # 2. 현재 위치(row, col)와 채워 넣을 숫자(num) 초기화
    # 시작 위치를 (-1, 0)으로 설정하여 첫 번째 이동(아래로)이 (0, 0)이 되도록 함
    y, x = -1, 0
    num = 1
    
    # 3. 방향 전환은 총 n번 일어남
    for i in range(n):
        # i를 3으로 나눈 나머지에 따라 방향 결정 (0: 아래, 1: 오른쪽, 2: 대각선 위)
        direction = i % 3
        
        # 4. 해당 방향으로 이동할 횟수 결정
        # 아래로 n번, 오른쪽 n-1번, 대각선 n-2번 ...
        for j in range(i, n):
            if direction == 0:      # 아래로 이동
                y += 1
            elif direction == 1:    # 오른쪽으로 이동
                x += 1
            else:                   # 대각선 위로 이동
                y -= 1
                x -= 1
            
            # 현재 위치에 숫자 채우기
            answer[y][x] = num
            num += 1
            
    # 5. 2차원 리스트를 1차원으로 펼쳐서 반환
    return [item for row in answer for item in row]
