def solution(n, arr1, arr2):
    a = []
    for i in range(len(arr1)):
        b=str(bin(arr1[i])[2:])
        
        while len(b) !=n:
            b='0'+b
        
        arr1[i]=b
    for i in range(len(arr2)):
        b=str(bin(arr2[i])[2:])
        
        while len(b) !=n:
            b='0'+b
        
        arr2[i]=b 
        
    print(arr1,arr2)
    for i in range(n):
        b=''
        for j in range(n):
            
            if arr1[i][j] =='1' or arr2[i][j] == '1':
                b+= '#'
            elif arr1[i][j] and arr2[i][j] =='0':
                b+= ' '
        a.append(b)      

    return a