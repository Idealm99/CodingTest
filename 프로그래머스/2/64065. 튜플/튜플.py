def solution(s):
    s= s[1:-1]+',}'

    a=[]
    ln=[]
    st=''
    for i in s :
        if i == '{':
            a=[]
            
        elif i == '}' :
            ln.append(a)
            
                
        elif i == ',' :
            a.append(int(st))
            st=''
        else:
            st+=i
            
    
   
    c=[0]*(len(ln)-1)
    for i in ln :
        c[len(i)-1]=i
        
    answer=[]
    dick={}
    for i in c :
        for j in i:
            if j not in answer :
                answer.append(j)
    
    return answer



# def solution(s):
#     # {{, }}를 제거 후 },{ 으로 나누기
#     data = s[2:-2].split("},{")
#     # 길이 별로 오름차순 정렬
#     data = sorted(data, key=lambda x: len(x))
#     answer = []
#     for item in data:
#         # 각각의 원소로 분류 후
#         item = list(map(int, item.split(",")))
#         for value in item:
#             # 포함되어 있지 않으면 input
#             if value not in answer:
#                 answer.append(value)
#     return answer