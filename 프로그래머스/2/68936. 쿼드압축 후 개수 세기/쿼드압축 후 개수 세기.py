def solution(arr):
    # 최종 0과 1의 개수를 저장할 리스트
    answer = [0, 0]

    def compress(x, y, size):
        # 현재 영역의 첫 번째 값
        start_val = arr[x][y]

        # 영역 전체가 같은 값인지 확인
        for i in range(x, x + size):
            for j in range(y, y + size):
                # 다른 값이 있다면, 4분할하여 재귀 호출
                if arr[i][j] != start_val:
                    new_size = size // 2
                    compress(x, y, new_size) # 1사분면
                    compress(x, y + new_size, new_size) # 2사분면
                    compress(x + new_size, y, new_size) # 3사분면
                    compress(x + new_size, y + new_size, new_size) # 4사분면
                    return # 재귀 호출 후 현재 함수는 종료

        # for 루프를 무사히 마쳤다면 모든 값이 같다는 의미
        # 해당 값의 카운트를 1 증가
        answer[start_val] += 1

    # 처음에는 전체 배열(0, 0, len(arr))로 시작
    compress(0, 0, len(arr))

    return answer