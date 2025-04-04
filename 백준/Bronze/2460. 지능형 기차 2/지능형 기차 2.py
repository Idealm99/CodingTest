n=10 
li=[]
for i in range(n) :
    a,b=map(int,input().split(' '))
    li.append([a,b])
sum = 0
max=0
for i in li :
    sum=sum+i[1]-i[0]
    if sum > max :
        max= sum

print(max)