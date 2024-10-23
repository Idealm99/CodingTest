#배울만한 코드 collection 의 deque 를 사용하면 더 빠름

def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time

# 내 코드

# def solution(cacheSize, cities):
#     if cacheSize == 0:
#         return 5 * len(cities)  # 캐시 크기가 0이면 모든 도시가 캐시 미스가 됨

#     cache = {}
#     current_time = 0  # 각 도시의 최근 사용 시간을 기록
#     total_time = 0

#     for city in cities:
#         city = city.lower()  # 도시 이름을 소문자로 변환

#         if city in cache:
#             # 캐시 히트: 이미 캐시에 있는 경우
#             total_time += 1
#         else:
#             # 캐시 미스: 캐시에 없는 경우
#             if len(cache) == cacheSize:  # 캐시가 가득 찬 경우
#                 # 가장 오래된 항목(즉, 가장 사용 시간이 오래된 도시)을 제거
#                 oldest_city = min(cache, key=cache.get)  # 사용 시간이 가장 적은 도시
#                 del cache[oldest_city]
#             total_time += 5

#         # 도시를 캐시에 추가하거나 업데이트 (최근 사용 시간 갱신)
#         cache[city] = current_time
#         current_time += 1

#     return total_time
