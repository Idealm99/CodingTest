def solution(ingredient):

    count =0
    li=[]

    for i in ingredient:
        li.append(i)
        if len(li) >=4 :
            if li[-4:] ==[1,2,3,1]:
                count+=1
                for _ in range(4):
                    del li[-1]

    return count