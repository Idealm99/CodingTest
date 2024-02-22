def solution(numbers, hand):
    re = ''
    w=[[1,2,3],[4,5,6],[7,8,9],[None,0,None]]
    l_h =[3,0]
    r_h=[3,2]
    for i in numbers :
        
        i_w=[]
        # 누를 버튼 위치 찾기
        for idx, row  in enumerate(w):
            if i in row : 
                i_w=[idx,row.index(i)]
                break
        if i in [1,4,7] :
            l_h=i_w
            re+="L"
            continue
        elif i in [3,6,9]:
            r_h=i_w
            re+="R"
            continue

        # 누를 번호와 왼,오른 손가락의 거리
        l=abs(l_h[0]-i_w[0])+abs(l_h[1]-i_w[1])
        r=abs(r_h[0]-i_w[0])+abs(r_h[1]-i_w[1])

        if l > r :
            r_h=i_w
            re+="R"
        elif r > l:
            l_h=i_w
            re+="L"
        else:
            if hand == "right":
                r_h=i_w
                re+="R"     
            else:
                l_h=i_w
                re+="L" 
        print(l_h,r_h)
            
    return re