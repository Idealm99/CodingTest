# 모법 답안 
# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer

from collections import Counter
def solution(citations):
    citations.sort()
    d= dict(Counter(citations))
    

    max=0
    for h in range(citations[-1]):
        sum=0
        for i in d.keys():
            if h<=i:
                sum+=d[i]
        if h <=sum :
            max=h
            
    return max   
            
            
        