def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)  # 캐시 크기가 0이면 모든 도시가 캐시 미스가 됨

    cache = []
    total_time = 0

    for city in cities:
        city = city.lower()  # 각 도시 이름을 소문자로 변환

        if city in cache:
            # 캐시 히트: 이미 캐시에 존재하는 경우
            cache.remove(city)  # 기존 항목을 제거하고
            cache.append(city)  # 최근에 사용된 항목을 뒤로 추가
            total_time += 1
        else:
            # 캐시 미스: 캐시에 존재하지 않는 경우
            if len(cache) == cacheSize :
                
                cache.pop(0)  # 캐시의 첫 번째 항목(오래된 항목)을 제거
            cache.append(city)  # 새로운 항목을 추가
            total_time += 5

    return total_time
