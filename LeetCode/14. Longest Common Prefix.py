class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=len(sorted(strs,key=len)[0])
        if a==0:
            return ''
        res=''
        r=0
        for c in range(a):
            f=0
            for r in range(1,len(strs)):
                if strs[r][c]==strs[r-1][c]:
                    f+=1
                    
                else:
                    break
            if f==len(strs)-1:
                res+=strs[r][c]        
            else:
           
                return res
        return res
        
