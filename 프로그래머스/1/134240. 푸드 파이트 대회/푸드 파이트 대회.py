def solution(food):
    st=''
    re=''
    food.pop(0)
    for idx,food_num in enumerate(food):
        count= food_num // 2
        st += str((idx+1))*count 
        re += str((idx +1))*count
        
    
    
    
    return re+'0'+st[::-1]