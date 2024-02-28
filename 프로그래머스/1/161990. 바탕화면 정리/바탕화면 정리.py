# 하나하나 구하는 것 보다 #의 위치를 모두 구해서 최대 최소로 구할 수 있음
# def solution(wall):
#     a, b = [], []
#     for i in range(len(wall)):
#         for j in range(len(wall[i])):
#             if wall[i][j] == "#":
#                 a.append(i)
#                 b.append(j)
#     return [min(a), min(b), max(a) + 1, max(b) + 1]
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