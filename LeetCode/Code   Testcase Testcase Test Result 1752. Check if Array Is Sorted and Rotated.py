class Solution:
    def check(self, nums: List[int]) -> bool:
        n=1
        if len(nums)==1:
            return True
        new_nums = nums+nums
        for i in range(1,len(new_nums)):
            if new_nums[i]>=new_nums[i-1]:
                n+=1
            else:
                n=1
            if n==len(nums):
                return True
        return False
            
