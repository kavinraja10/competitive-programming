class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current_sum = sum_ = nums[0]
        i=1
        while i<len(nums):
            if nums[i]>nums[i-1]:
                current_sum+=nums[i]
            else:
                current_sum=nums[i]
            if current_sum>sum_:
                sum_ = current_sum
            i+=1
        return sum_

        


