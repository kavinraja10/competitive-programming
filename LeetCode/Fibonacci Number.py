class Solution:
    def fib(self, n: int) -> int:
        f1=0
        f2=1
        f3=1
        if n==f1 or n==f2:
            return n
        for i in range(2,n+1):
            f3=f1+f2
            f1=f2
            f2=f3
        return f3
