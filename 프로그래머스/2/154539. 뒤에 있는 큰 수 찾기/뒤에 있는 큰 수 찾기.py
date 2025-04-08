def solution(numbers):
    stack=[]
    result=[]
    while len(numbers) >0  :
        
        if len(stack) ==0  :
            stack.append(numbers.pop())
            result.append(-1)
        elif stack[-1] <= numbers[-1] :
            stack.pop()
        else:
            result.append(stack[-1])
            stack.append(numbers.pop())
    return list(reversed(result))
    