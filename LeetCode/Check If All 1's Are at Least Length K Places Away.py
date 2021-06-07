class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        c=0
        flag=0
        for i in nums:
            if i == 1 and flag==0:
                flag=10
                continue
            if flag==10:
                if i==1:
                    if c>=k:
                        c=0
                        pass
                    else:
                        return False
                else:
                    c+=1
        return True
