def solution(phone_book):
    phone_dict = {}
    for number in phone_book:
        phone_dict[number] = True
        
    for number in phone_book:
        prefix = ''
        for ch in number[:-1]:
            prefix += ch
            if prefix in phone_dict:
                return False
    return True
