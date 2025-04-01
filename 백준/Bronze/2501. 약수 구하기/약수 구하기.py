n, k = input().split(' ')
n=int(n)
k= int(k)
i=1
li=[]
while i <= n :
    if n % i ==0 :
        li.append(i)
    i+=1

if len(li) < k :
     print(0)
else :
    print(li[k-1])
