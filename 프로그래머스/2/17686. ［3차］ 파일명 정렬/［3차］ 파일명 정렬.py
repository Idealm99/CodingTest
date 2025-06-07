def solution(files):
    li = []
    for idx, i in enumerate(files):
        flag = True 
        num = ''
        
        for jdx, j in enumerate(i):
            if j in ['0','1','2','3','4','5','6','7','8','9']:
                num += j
                flag = False
            elif flag:
                continue
            else:
                break
        
        # 파일명을 HEAD, NUMBER, TAIL로 분리
        head = i[:i.index(num)] if num else i
        number = int(num) if num else 0
        tail = i[i.index(num) + len(num):] if num else ''
        
        li.append([head.lower(), number, tail, idx])  # head는 대소문자 구분 없이 비교
    
    # HEAD(대소문자 구분 없음) 기준으로 먼저 정렬, 그 다음 NUMBER 기준으로 정렬
    li.sort(key=lambda x: (x[0], x[1]))
    
    # 원본 파일명만 반환
    return [files[item[3]] for item in li]