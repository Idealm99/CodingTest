def solution(s, n):
    a=''
    for i in s :
        if i != ' ':
            if ord(i)>= 97:   # a 의 아스키 코드 97 i가 소문자냐 대문자냐
                if 123>ord(i)+n:         
                    a+=chr(ord(i)+n)
                else: 
                    a+=chr((ord(i)+n-ord('a'))%26+ord('a'))

            else: 
                if 91>ord(i)+n:
                    a+=chr((ord(i)+n))
                else:
                    a+=chr((ord(i)+n-ord('A'))%26+ord('A'))
                
        else:
            a+=' '

    return a