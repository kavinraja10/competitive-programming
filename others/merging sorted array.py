'''
Given two sorted arrays, merge them such that the elements are not repeated

Input:
        Array 1: 2,4,5,6,7,9,10,13
        Array 2: 2,3,4,5,6,7,8,9,11,15
Output:
       Merged array: 2,3,4,5,6,7,8,9,10,11,13,15 
'''
l1=[2,4,5,6,7,9,10,13]
l2=[2,3,4,5,6,7,8,9,11,15]
res=[]
i=0
j=0
while i<len(l1) and j<len(l2):
    print(i,j)
    if l1[i] >l2[j]:
        res.append(l2[j])
        j+=1
    elif l1[i] ==l2[j]:
        res.append(l2[j])
        res.append(l2[j])
        j+=1
        i+=1
    else:
        res.append(l1[i])
        i+=1
if i<len(l1)-1:
    res=res+l1[i:]
else:
    res=res+l2[j:]
print(res)
    
