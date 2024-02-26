def solution(data, ext, val_ext, sort_by):
    dict ={ 'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    li=[]

    for i in data :
        if i[dict[ext]] < val_ext :
            li.append(i)
    
    sorted_li = sorted(li, key=lambda x: x[dict[sort_by]])
    return sorted_li
