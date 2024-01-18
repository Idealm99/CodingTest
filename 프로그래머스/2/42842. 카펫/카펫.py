def solution(brown, yellow):
    x=1
    flag =True
    while flag :
        y= yellow // x
        if yellow % x == 0 and y <= x and 2 * ( x+y+2) == brown:
            flag = False
            return [x+2,y+2]
        else :
            x +=1