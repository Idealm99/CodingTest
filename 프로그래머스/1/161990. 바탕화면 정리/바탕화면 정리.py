def solution(wallpaper):
    answer = []
    # up,left,down,right 순서대로 출력해야함
    up=-1
    right=0
    left=51
    down=0
    for idx,i in enumerate(wallpaper) :
        if up== -1 :
            if '#' in i:
                up=idx
                down =idx
                left = min(left,i.index('#'))
        else:
            if '#' in i :
                down=idx
                left = min(left,i.index('#'))
        
        
        for j in range(0,len(i)):
            if i[j]=='#':
                right=max(right,j)
    
    return [up,left,down+1,right+1]