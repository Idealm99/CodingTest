# def rank_elements(lst):
#     # 리스트를 내림차순으로 정렬한 후, 각 요소의 인덱스를 반환합니다.
#     sorted_indices = [i for i, _ in sorted(enumerate(lst), key=lambda x: x[1], reverse=True)]
#     return sorted_indices
# def solution(k, dungeons):
#     dict={}
#     li=[]
#     for i,j in dungeons:
#         li.append(i-j)
#         if i not in dict :
#             dict[i]= j
#         else:
#             if dict[i] > j :
#                 dict[i] =j
#     rank=rank_elements(li)
#     sum=0
#     for i in rank:
#         if k >= dungeons[i][0]:
#             k-=dungeons[i][1]
#             sum+=1
#     return sum
from itertools import permutations

def solution(k, dungeons):
    max_explored = 0
    
    # 모든 던전 탐험 순서를 생성합니다.
    for order in permutations(dungeons):
        current_fatigue = k
        explored = 0
        
        # 던전을 탐험하면서 최대 탐험 가능한 수를 계산합니다.
        for min_fatigue, consume_fatigue in order:
            if current_fatigue >= min_fatigue:
                current_fatigue -= consume_fatigue
                explored += 1
            else:
                break
        
        max_explored = max(max_explored, explored)
    
    return max_explored

    