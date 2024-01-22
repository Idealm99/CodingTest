def solution(sizes):
    가로=0
    세로=0
    for idx in range(len(sizes)):
        if sizes[idx][1] > sizes[idx][0]:
            sizes[idx][1] , sizes[idx][0] = sizes[idx][0], sizes[idx][1]
        가로=max(가로,sizes[idx][0])
        세로=max(세로,sizes[idx][1])
    return 가로*세로
    
    