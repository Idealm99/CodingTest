def solution(numbers):
    from functools import cmp_to_key
    
    li = [str(i) for i in numbers]
    li.sort(key=cmp_to_key(lambda x, y: -1 if x+y > y+x else 1))
    
    return str(int(''.join(li)))

        
        