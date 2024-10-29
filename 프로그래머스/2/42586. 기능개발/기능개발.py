from collections import Counter

def solution(progresses, speeds):
    li = []
    for i, n in enumerate(progresses):
        if (100 - n) // speeds[i] != (100 - n) / speeds[i]: 
            li.append((100 - n) // speeds[i] + 1)
        else:
            li.append((100 - n) // speeds[i])

    for i in range(len(li) - 1):
        if li[i] >= li[i + 1]:
            li[i + 1] = li[i]
            
    return list(Counter(li).values())
