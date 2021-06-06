class Solution:
    def climbStairs(self, n: int) -> int:
        l=[1,2]
        if n==1:
            return 1
        while len(l)<n:
            l.append(l[(len(l)-1)]+l[(len(l)-2)])
        return (l[len(l)-1])    
