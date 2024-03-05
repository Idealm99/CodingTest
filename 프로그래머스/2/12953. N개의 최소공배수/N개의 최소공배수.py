def solution(arr):
    dict={}
    for num in arr :
        i=2
        li=[]
        while num >1 :
            if num % i ==0:
                num /= i
                li.append(i)
                i=2
            else:
                i+=1
        for j in set(li):
            if j in dict:
                dict[j]=max(dict[j],li.count(j))
            else:
                dict[j]=li.count(j)
    re=1
    for i in list(dict.keys()):
        sum=1
        for _ in range(dict[i]):
            sum*=i
        re*=sum
    return re