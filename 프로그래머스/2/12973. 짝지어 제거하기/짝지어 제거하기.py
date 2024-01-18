def solution(s):
    stack = []  # 중복 문자를 저장할 스택

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # 스택의 맨 위 문자와 현재 문자가 같다면 제거
        else:
            stack.append(char)  # 스택에 추가

    if not stack:
        return 1  # 스택이 비어있다면 모든 문자가 제거됨
    else:
        return 0  # 아직 남은 문자가 있다면 중복 문자가 남아있음
