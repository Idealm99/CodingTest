def solution(n, stations, w):
    answer = 0
    coverage_ranges = []
    
    # 기존 기지국들의 커버리지 범위 계산
    for station in stations:
        left = max(1, station - w)  # 최소 1
        right = min(n, station + w)  # 최대 n
        coverage_ranges.append((left, right))
    
    # 커버되지 않는 구간들 찾기
    uncovered_sections = []
    current_pos = 1
    
    for left, right in coverage_ranges:
        if current_pos < left:
            # 커버되지 않는 구간 발견
            uncovered_sections.append((current_pos, left - 1))
        current_pos = max(current_pos, right + 1)
    
    # 마지막 구간 체크
    if current_pos <= n:
        uncovered_sections.append((current_pos, n))
    
    # 각 커버되지 않는 구간에 필요한 기지국 수 계산
    coverage_range = 2 * w + 1  # 하나의 기지국이 커버할 수 있는 범위
    
    for start, end in uncovered_sections:
        section_length = end - start + 1
        needed_stations = (section_length + coverage_range - 1) // coverage_range  # 올림 계산
        answer += needed_stations
    
    return answer