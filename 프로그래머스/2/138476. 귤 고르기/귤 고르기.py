
# import collections
# cnt = collections.Counter(tangerine)
# 위 코드로 유닛의 개수를 한번에 구할 수 있다.

def solution(k, tangerine):
    
    
    dict={}
    for i in tangerine:
        if i in dict :
            dict[i]+=1
        else:
            dict[i]=1
    li=list(dict.values())
    li.sort(reverse=True)
    if li[0] >= k:
        return 1
    
    count=0
    for i in li :
        k-=i
        count+=1
        if k<=0 :
            return count
                
                
            
