'''
Given a list of numbers and a number k, return whether any two
numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return
true since 10 + 7 is 17
'''
l=[10, 15, 3, 7]
k=200
l.sort()
i=0
j=len(l)-1
while i<j:
    if l[i]+l[j]<k:
        i+=1
    elif l[i]+l[j]>k:
        j-=1
    elif l[i]+l[j]==k:
        print(l[i],l[j])
        break
else:
    print('not found')
