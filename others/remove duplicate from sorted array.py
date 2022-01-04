# remove duplicate from sorted array

l=[1,1,2,4,5,6,6]
n=len(l)
for i in range(n-1):
    if l[i]==l[i+1]:
        n-=1
print(n)
