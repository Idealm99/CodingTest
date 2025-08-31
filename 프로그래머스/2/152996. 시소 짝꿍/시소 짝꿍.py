def solution(weights):
    answer = 0
    weight_counts = {}  # key: 무게, value: 등장 횟수

    # 1. 무게 배열을 정렬
    for w in sorted(weights):
        # 2. 현재 무게(w)와 짝이 될 수 있는 이전 무게들을 딕셔너리에서 찾는다
        
        # 1:1 비율
        if w in weight_counts:
            answer += weight_counts[w]
        
        # 2:3 비율 (파트너 * 3 == w * 2)
        if (w * 2) % 3 == 0 and (w * 2 // 3) in weight_counts:
            answer += weight_counts[w * 2 // 3]
            
        # 1:2 비율 (파트너 * 2 == w * 1)
        if w % 2 == 0 and (w // 2) in weight_counts:
            answer += weight_counts[w // 2]
            
        # 3:4 비율 (파트너 * 4 == w * 3)
        if (w * 3) % 4 == 0 and (w * 3 // 4) in weight_counts:
            answer += weight_counts[w * 3 // 4]

        # 3. 현재 무게를 딕셔너리에 기록 (다음 원소들이 볼 수 있도록)
        weight_counts[w] = weight_counts.get(w, 0) + 1
        # print(weight_counts)
    return answer