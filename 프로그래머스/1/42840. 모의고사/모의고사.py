def solution(answers):
    a=[1,2,3,4,5]*((len(answers)//5)+1)
    b=[2,1,2,3,2,4,2,5]*((len(answers)//8)+1)
    c=[3,3,1,1,2,2,4,4,5,5]*((len(answers)//10)+1)

    a_score=0
    b_score=0
    c_score=0
    for i in range(len(answers)) :                  
        if answers[i] == a[i]: 
                 a_score+=1
        if answers[i] == b[i]: 
                 b_score+=1
        if answers[i] == c[i]: 
                 c_score+=1
                   
    li=[a_score,b_score,c_score]
    re=[]
    print(li)
    for i in range(len(li)):
        if li[i]-max(li) == 0 :
            re.append(i+1)
    return re
            
