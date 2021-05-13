class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a=sorted(list(set(nums)),reverse=True)
        #print(a)
        if len(a)<3:
            return (a[0])
        else:
            return (a[2])
