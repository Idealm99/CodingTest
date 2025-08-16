def solution(sequence, k):
    start = 0
    end = 0
    # min_len의 초기값을 sequence 길이보다 큰 값으로 설정
    min_len = len(sequence) + 1 
    sequence_sum = 0
    result = []
    
    while end < len(sequence):
        sequence_sum += sequence[end]
        
        # 합이 k보다 크거나 같으면 start를 이동시킬 차례
        while sequence_sum >= k:
            # 만약 합이 정확히 k라면, 길이 비교 후 정답 갱신
            if sequence_sum == k:
                if min_len > end - start + 1:
                    min_len = end - start + 1
                    result = [start, end]
            
            # start 포인터를 오른쪽으로 이동
            sequence_sum -= sequence[start]
            start += 1
            
        # end 포인터를 오른쪽으로 이동
        end += 1
            
    return result