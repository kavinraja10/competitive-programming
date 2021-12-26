class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        l=0
        res=''
        for i in s:
            if i in res:
                l=max(l,len(res))
                res=res[res.find(i)+1:]+i
                print(res)
            else:
                res+=i
        return max(l,len(res))
