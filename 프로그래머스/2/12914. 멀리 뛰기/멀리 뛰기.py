def solution(n):
    # 1칸 뛰는 경우의 수
    one_step = 1
    # 2칸 뛰는 경우의 수
    two_step = 2

    if n == 1:
        return one_step
    elif n == 2:
        return two_step

    # n이 3 이상인 경우
    for _ in range(3, n + 1):
        # 이전에 계산된 경우의 수를 이용하여 현재 경우의 수 계산
        current_step = (one_step + two_step) % 1234567
        # 다음 계산을 위해 이전 값 갱신
        one_step, two_step = two_step, current_step

    return current_step % 1234567

# 테스트
print(solution(4))  # 출력 결과는 5
