class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c=0
        f=sorted(heights)
        for i in range(len(heights)):
            if heights[i]!=f[i]:
                c+=1
        return(c)
                
