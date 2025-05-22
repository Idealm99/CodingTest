def solution(skill, skill_trees):
    dic={}
    for idx, s in enumerate(skill):
        dic[s]=idx
    
        
    count =0
    l=len(skill)
    for i in skill_trees:
        memory=[False]*l
        flag=True
        # print('\n스킬 트리 ',i)
        for n in i :
            # print('n: ',n)
            if n in dic.keys() :
                # print('n in dic')
                # print(memory)
                if True in memory[dic[n]:] or False in memory[:dic[n]]:
                    # print('잘못된 스킬배움')
                    flag =False
                    break
                else: memory[dic[n]] =True
        if flag :
            # print('\n카운트 증가')
            count+=1
    
    return count