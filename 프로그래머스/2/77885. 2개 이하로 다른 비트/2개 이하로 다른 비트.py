def solution(numbers):
    def find_next(n):
        # 현재 숫자의 비트에서 가장 오른쪽에 있는 0을 찾기
        bit_pos = 0
        temp = n
        
        # 가장 오른쪽 0의 위치 찾기
        while temp & 1:
            bit_pos += 1
            temp >>= 1
        
        # 해당 위치의 0을 1로 바꾸기
        result = n | (1 << bit_pos)
        
        # 그 오른쪽에 있던 1들 중 가장 오른쪽 하나를 0으로 바꾸기
        if bit_pos > 0:
            result &= ~(1 << (bit_pos - 1))
        
        return result
    
    return [find_next(num) for num in numbers]