def solution(sticker):
    n = len(sticker)
    
    # 스티커가 1개일 경우, 그 값 자체가 최댓값입니다.
    if n == 1:
        return sticker[0]
    
    # 선형 배열에서의 최댓값을 구하는 도우미 함수
    def linear_solution(arr):
        if not arr:
            return 0
        if len(arr) == 1:
            return arr[0]
        
        # dp[i] = i번째 위치까지의 스티커를 뜯어 얻을 수 있는 최대 합
        dp = [0] * len(arr)
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        
        for i in range(2, len(arr)):
            # 현재 위치(arr[i])의 스티커를 뜯는 경우: arr[i] + dp[i-2]
            # 현재 위치의 스티커를 뜯지 않는 경우: dp[i-1]
            # 두 경우 중 더 큰 값을 선택
            dp[i] = max(dp[i-1], arr[i] + dp[i-2])
            
        return dp[-1]

    # 경우 1: 첫 번째 스티커를 뜯는 경우 (마지막 제외)
    case1 = linear_solution(sticker[0:n-1])
    
    # 경우 2: 첫 번째 스티커를 뜯지 않는 경우 (마지막 포함)
    case2 = linear_solution(sticker[1:n])
    
    # 두 경우 중 더 큰 값을 반환
    return max(case1, case2)