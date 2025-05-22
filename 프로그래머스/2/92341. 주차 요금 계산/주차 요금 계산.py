from math import ceil

def solution(fees, records):
    import collections
    
    # 1. 차량별 입출차 기록 누적
    car_dict = collections.defaultdict(list)
    for rec in records:
        time, car, action = rec.split()
        car_dict[car].append((time, action))
    
    # 2. 각 차량별 총 주차 시간 계산
    total_time = {}
    for car in car_dict:
        times = car_dict[car]
        total = 0
        stack = []
        for time, action in times:
            if action == 'IN':
                stack.append(time)
            else: # OUT
                in_time = stack.pop()
                in_h, in_m = map(int, in_time.split(':'))
                out_h, out_m = map(int, time.split(':'))
                total += (out_h*60+out_m) - (in_h*60+in_m)
        # 출차기록이 없는 경우 23:59 출차로 간주
        if stack:
            in_time = stack.pop()
            in_h, in_m = map(int, in_time.split(':'))
            out_h, out_m = 23, 59
            total += (out_h*60+out_m) - (in_h*60+in_m)
        total_time[car] = total

    # 3. 요금 계산
    basic_time, basic_fee, unit_time, unit_fee = fees
    answer = []
    for car in sorted(total_time):
        t = total_time[car]
        if t <= basic_time:
            answer.append(basic_fee)
        else:
            answer.append(basic_fee + ceil((t-basic_time)/unit_time)*unit_fee)
    return answer
