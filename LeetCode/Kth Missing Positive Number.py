class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        c=0
        i=1
        while i<len(arr)+1 + k: 
            if i in arr:
                pass
            else:
                c+=1
                print(i)
            if c==k:
                return i
            i=i+1
