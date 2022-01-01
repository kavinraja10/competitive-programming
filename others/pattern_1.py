'''
Write a program to print the following output for the given input. You can assume the string is of odd length

Eg 1: Input: 12345
       Output:
1       5
  2   4
    3
  2  4
1      5
'''
s="12345"
s=list(s)
n=len(s)//2+1
l=0
r=len(s)-1
for i in range(n):
        for j in range(len(s)):
            if j==l or j==r:
                if l==r:
                    print(s[l] ,end='')
                    break
                
                print(s[j] ,end='')
            else:
                print(' ',end='')
        print()
        l+=1
        r-=1
n=n-1
l=l-2
r=r+2
for i in range(n):
        for j in range(len(s)):
            if j==l or j==r:
                if l==r:
                    print(s[l] ,end='')
                    break
                
                print(s[j] ,end='')
            else:
                print(' ',end='')
        print()
        l-=1
        r+=1
                
        
