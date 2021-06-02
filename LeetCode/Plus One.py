class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        s=''.join(list(map(str,digits)))
        return list(map(int(list(str(int(s)+1)))
