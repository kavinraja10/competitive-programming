'''
Given an array of integers of size, N. Assume ‘0’
as the invalid number and all others as a valid number.
Write a program that modifies the array in such a way that
if the next number is a valid number and is the same as the
current number, double the current number value and replace the
next number with 0. After the modification, rearrange the array
such that all 0’s are shifted to the end and the sequence of the
valid number or new doubled number is maintained as in the original array.

Example 1:

Input : arr[ ] = {2, 2, 0, 4, 0, 8}
Output : 4 4 8 0 0 0

'''
arr=[0, 2, 2, 2, 0, 6, 6, 0, 0, 8]
n=len(arr)
i=0
while i<(n-1):
        if arr[i]!=0:
            arr[i]=arr[i]*arr[i]
        else:
            
            j=1
            while 1:
                if i+j>n-1:
                    break
                if arr[i+j]==0:
                    j+=1
                else:
                    arr[i],arr[i+j]=arr[i+j],0
                    break
            i+=1
print(arr)
