def solution(prices):
    result = []
    for i in range(len(prices)):
        count = 0
        for j in range(i + 1, len(prices)):
            count += 1
            if prices[j] < prices[i]:
                break
        result.append(count)
    return result
