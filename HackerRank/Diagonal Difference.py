def diagonalDifference(arr):
    # Write your code here
    #to find first sum
    s=0
    a=0
    for i in range(len(arr)):
        s+=arr[i][a] 
        a+=1
    a=len(arr)-1
    s1=0
    for i in range(len(arr)):
        s1+=arr[i][a]
        a-=1
    return abs(s-s1)
        
