t = int(input())  # 테스트 케이스 개수
n = [int(input()) for _ in range(t)]  # 각 줄마다 정수 하나 입력받기

for i in range(t):
    now = n[i]
    count = 0
    while now >= 1:
        if now % 2 == 1:
            print(count, end=' ')  # 줄바꿈 없이 출력
        count += 1
        now //= 2
    print()  # 각 테스트 케이스 끝나면 줄바꿈
