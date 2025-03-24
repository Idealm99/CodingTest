from collections import Counter 

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    A = []
    B = []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            A.append(str1[i] + str1[i + 1])

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            B.append(str2[i] + str2[i + 1])

    counterA = Counter(A)
    counterB = Counter(B)

    intersection = counterA & counterB
    union = counterA | counterB

    s = sum(intersection.values())
    u = sum(union.values())

    if u == 0:
        return 65536

    return int(s / u * 65536)
