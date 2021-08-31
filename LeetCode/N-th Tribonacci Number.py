class Solution:
    def tribonacci(self, n: int) -> int:
        a=0
        b=1
        c=1
        if n==a or n==b :
            return n
        if  n==2:
            return 1
        for i in range(n-2):
            s=a+b+c
            a=b
            b=c
            c=s
        return s
