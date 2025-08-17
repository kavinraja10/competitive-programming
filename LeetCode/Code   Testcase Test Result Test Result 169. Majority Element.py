class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        majority = 0
        value = 0
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
            if majority<count[i]:
                majority = count[i]
                value = i
        return  value
            
       
