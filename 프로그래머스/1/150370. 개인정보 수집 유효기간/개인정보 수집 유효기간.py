def solution(today, terms, privacies):
    # 주어진 날짜를 연, 월, 일로 분리
    t_year, t_month, t_day = map(int, today.split('.'))
    # 결과를 담을 리스트
    t_sum= t_day + t_month * 28 + t_year * 12 * 28
    to_be_deleted = []
    count=1

    # 개인정보를 하나씩 확인
    for privacy in privacies:
        flag = privacy[-1]
        privacy = privacy[:-1]
        # 개인정보의 수집일을 연, 월, 일로 분리
        year, month, day = map(int, privacy.split('.'))
        sum= day + month * 28 + year * 12 * 28 -1
        # 해당 약관의 유효기간을 계산
        for term in terms:
          flag2, contract =term.split(' ')
          if flag == flag2 :
            sum += int(contract) *28
            if t_sum > sum :
             to_be_deleted.append(count)
             break
        count +=1
    return to_be_deleted
