class Solution:
    def guessNumber(self, n: int) -> int:
        # if n in (1,2):
        #     return n
        i=0
        while i<n:
            mid=(i+n)//2
            g=guess(mid)
            if not g:
                return mid
            elif g==-1:
                n=mid
            else:
                i=mid+1
