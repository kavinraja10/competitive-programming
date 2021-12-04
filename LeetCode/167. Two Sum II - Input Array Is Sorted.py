class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r=len(numbers)-1
        l=0
        while l<r:
            print(l,r)
            if (numbers[l]+numbers[r])>target:
                r-=1
            elif (numbers[l]+numbers[r])<target:
                l+=1
            else:
                print(100)
                return [l+1,r+1]
                break
                
