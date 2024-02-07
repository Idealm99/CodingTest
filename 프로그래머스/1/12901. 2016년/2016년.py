# import datetime

# def solution(a, b):
#     days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
#     # 월과 일을 올바르게 사용
#     sum = datetime.datetime(2016, a, b) - datetime.datetime(2016, 1, 1)
#     a = str(sum).split(' ')
#     return days[int(a[0]) % 7]
def solution(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]