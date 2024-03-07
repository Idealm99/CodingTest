def solution(n):
    count=0
    for i in range(4,n+1):
        s=0
        for j in range(2,i+1):
            if i%j ==0:
                s+=1
        if s >= 2:
            print(i)
            count+=1
    return count


# def solution(n):
#     output = 0
#     for i in range(4, n + 1):
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 output += 1
#                 break
#     return output
