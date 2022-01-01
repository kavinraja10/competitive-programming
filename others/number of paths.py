'''
The problem is to count all the possible paths from top left to bottom right of a
MxN matrix with the constraints that from each cell you can either move to right or down.

Example 1:

Input:
M = 3 and N = 3
Output: 6
Explanation:
Let the given input 3*3 matrix is filled 
as such:
A B C
D E F
G H I
The possible paths which exists to reach 
'I' from 'A' following above conditions 
are as follows:ABCFI, ABEHI, ADGHI, ADEFI, 
ADEHI, ABEFI
'''
m=3
n=2
if n==1 or m==1:
    print(1)
else:
    dp=[[1,1,1]]
    for i in range(1,m):
        l=[]
        for j in range(n):
            if j==0:
                l.append(1)
            else:
                k=l[j-1]+dp[i-1][j]
                l.append(k)
        dp.append(l)
    print(dp[m-1][n-1])
