
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

# def solution(people, limit) :
#     answer = 0
#     people.sort()

#     a = 0
#     b = len(people) - 1
#     while a < b :
#         if people[b] + people[a] <= limit :
#             a += 1
#             answer += 1
#         b -= 1
#     return len(people) - answer
        
    
    
            


    