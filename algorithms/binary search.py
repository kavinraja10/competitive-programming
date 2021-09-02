def search(nums,target):
        left=0
        right=len(nums)-1
        mid=(left+right)//2
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return -1
print(search([-5,-1,0,3,5,9,10,12,13,34,],21))
