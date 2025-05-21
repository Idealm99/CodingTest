def solution(order):
    li = [i for i in range(len(order), 0, -1)]
    sub = []
    count = 0
    idx = 0  # order 인덱스

    while li or sub:
        if li and li[-1] == order[idx]:
            li.pop()
            count += 1
            idx += 1
        elif sub and sub[-1] == order[idx]:
            sub.pop()
            count += 1
            idx += 1
        elif li:
            sub.append(li.pop())
        else:
            break

        if idx >= len(order):
            break

    return count
