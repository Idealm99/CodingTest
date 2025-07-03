def solution(routes):
    # 1. 구간을 끝점 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    
    camera_count = 0
    camera_position = float('-inf')  # 현재 카메라 위치
    
    for start, end in routes:
        # 2. 현재 구간이 카메라로 커버되지 않는 경우
        if start > camera_position:
            
            camera_count += 1
            camera_position = end
    
    return camera_count
