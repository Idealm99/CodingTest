
def solution(people, limit):
    count=0
    n=len(people)
    people = sorted(people, reverse=True)
    li=[0]*n
    i , j = 0 , n-1
    while j>i :
        li[i]=1
        
        if limit >= people[j]+people[i]:
            li[j]=1
            j-=1
        i+=1
        count+=1
    if li[j]==0:
        count+=1
    return count
            
# def solution(people, limit):
#     count=0
#     n=len(people)
#     people.sort(reverse=True)
#     l=[0]*n
#     i,j=0,n-1

#     while j>i:
#         w=people[i]+people[j]
#         l[i]=1
#         i+=1
#         if w<=limit:
#             l[j]=1
#             j-=1
#         count+=1

#     if l[j]==0:
#         count+=1

#     return count
        
    
    
            


    