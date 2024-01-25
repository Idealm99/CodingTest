def solution(s):
    dick = {}
    li =[]
    for idx, ap in enumerate(s):
        if ap in dick:
            li.append(idx-dick[ap])
            
        else:
            li.append(-1)
        dick[ap]=idx
    return li

# def solution(s):
#     answer = []
#     dic = dict()
#     for i in range(len(s)):
#         if s[i] not in dic:
#             answer.append(-1)
#         else:
#             answer.append(i - dic[s[i]])
#         dic[s[i]] = i

#     return answer