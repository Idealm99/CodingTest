def solution(s):
    pair={']':'[','}':'{',')':'(' }
    
    count=0
    for x in range(len(s)):
        st=s[x:]+s[:x]
        stack=[]
        for i in st:
            if i in pair:
                if len(stack) !=0 and stack[-1] ==pair[i]:
                    stack.pop()
                else:
                    stack.append(None)
                    break
            else:
                stack.append(i)
        if len(stack)==0:
            count+=1
        
    return count