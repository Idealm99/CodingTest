def solution(n):
    re=[]
    def hanoi(n, start, mid, end):
        if n == 1:
            # 맨 위의 원판을 옮깁니다.
            re.append([start,end])
        else:
        # 맨 위의 원판을 제외한 나머지 N-1개의 원판을 맨 왼쪽 기둥에서 맨 가운데 기둥으로 옮깁니다.
         hanoi(n-1, start, end, mid)
        # 맨 위의 원판을 맨 오른쪽 기둥으로 옮깁니다.
         re.append([start,end])
        # N-1개의 원판을 맨 가운데 기둥에서 맨 오른쪽 기둥으로 옮깁니다.
         hanoi(n-1, mid, start, end)
    hanoi(n,1,2,3)
    return re
