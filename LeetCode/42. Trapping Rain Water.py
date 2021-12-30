class Solution:
    def trap(self, l: List[int]) -> int:

        if len(l)<3:
            return 0
        if l[0]>l[1]:
            pass
        else:
            for i in range(1,len(l)):
                if l[i-1]<l[i]:
                    pass
                else:
                    break

            #print(i)
            l=l[i-1:]
        for j in range(len(l)-1,-1,-1):
            if l[j-1]>l[j]:
                pass
            else:
                break
        l=l[:j+1]
        s=0
    
        for i in range(1,len(l)-1):
            le=max(l[:i+1])
            r=max(l[i::])
            m=min(le,r)
            #print(le,r,m)
            s+=(m-l[i])

        return (s)

