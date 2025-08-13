class Solution:
    def missingNumber(self, nums: List[int]) -> int:
          sum_ = sum(nums)
          n = len(nums)
          sum_of_range = (n*(n+1))//2
          return sum_of_range - sum_
