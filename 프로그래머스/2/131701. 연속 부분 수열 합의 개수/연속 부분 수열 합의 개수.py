def solution(elements):
    li=[]
    a=len((elements))
    for num in range(1,a+1):
         for i in range(0,a):
            if i+num > a:
                
                li.append(sum(elements[i:a]+elements[0:i+num-a]))
            else:
                li.append(sum(elements[i:i+num]))
    return len(set(li))
                   


    