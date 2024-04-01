from itertools import combinations


# def solution(clothes):
#     dict={}
#     for i in clothes:
#         if i[1] in dict :
#             dict[i[1]]+=1
#         else:
#             dict[i[1]] = 1
#     key=dict.keys()
    
#     count=len(clothes)
#     # 옷 종류의 개수
#     for i in range(2,len(key)+1):
        
#         a= combinations(key,i)
        
        
#         for j in a :
#             sum=1
            
#             for k in list(j) :
                
#                 sum*=dict[k]
            
#             count+=sum
            
#     return count
from collections import defaultdict

def solution(clothes):
    # 각 종류의 옷이 몇 개 있는지를 defaultdict를 사용해 카운트합니다.
    counts = defaultdict(int)
    for item, category in clothes:
        counts[category] += 1

    # 가능한 조합의 총 수를 계산합니다.
    total_combinations = 1
    for count in counts.values():
        # 각 종류의 옷을 입지 않는 경우를 고려하여 1을 더합니다.
        total_combinations *= (count + 1)

    # 모든 옷을 입지 않는 경우를 고려하여 1을 빼줍니다.
    return total_combinations - 1
        
            
        
        
    