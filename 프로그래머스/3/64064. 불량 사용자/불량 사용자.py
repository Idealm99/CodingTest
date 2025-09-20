from itertools import permutations
# def check(user_tuple, banned_list):
#     # 각 user_id와 banned_id 쌍을 순회
#     for u, b in zip(user_tuple, banned_list):
#         # 1. 두 아이디의 길이가 다르면 즉시 False 반환
#         if len(u) != len(b):
#             return False
        
#         # 2. 각 문자를 비교
#         for u_char, b_char in zip(u, b):
#             # banned_id의 문자가 '*'가 아니고, 두 문자가 다르면 False
#             if b_char != '*' and u_char != b_char:
#                 return False
                
#     # 3. 모든 쌍이 모든 검사를 통과했을 때만 True 반환
#     return True
def check(user_tuple, banned_list):
    for u ,b in zip(user_tuple,banned_list):
        if len(u) != len(b):
            return False
        for us,bs in zip(u,b):
            if bs!='*' and us != bs:
                return False
    return True

def solution(user_id, banned_id):
    # 1. user_id로 만들 수 있는 모든 순열 생성
    user_permutations = permutations(user_id, len(banned_id))
    
    # 3. 유효한 조합을 저장할 set 생성
    answer_set = set()
    
    # 2. 각 순열을 순회하며 매칭 확인
    for p in user_permutations:
        if check(p, banned_id):
            # 4. 매칭되면 정렬해서 set에 추가 (중복 제거)
            answer_set.add(tuple(sorted(p)))
            
    # 5. set의 크기를 반환
    return len(answer_set)