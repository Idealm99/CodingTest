def solution(wallet, bill):
    answer = 0
    w_max= max(wallet)
    w_min = min(wallet)
    
    b_max= max(bill)
    b_min= min(bill)
    
    while max(bill)> w_max or  min(bill)> w_min:
        bill[bill.index(max(bill))]=max(bill)//2
        answer +=1 

    return  answer

# def solution(wallet, bill):
#     cnt = 0
#     max_w, min_w = max(wallet), min(wallet)

#     while max_w < max(bill) or min(bill) > min_w :
#         bill[bill.index(max(bill))] = max(bill)//2
#         cnt += 1

#     return cnt