def solution(id_list, report, k):
    reports = {}# 신고 내역을 저장하는 딕셔너리


    for i in set(report):  # 중복된 신고 제거
        reporter, reported = i.split(' ')       
        reports.setdefault(reported, []).append(reporter)


    result_list=[0]*len(id_list)

    for idx, name in enumerate(id_list):
        if name in reports and len(reports[name]) >= k:
            for i in reports[name] :
                result_list[id_list.index(i)] +=1
    

    return result_list
