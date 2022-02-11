class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid) == True: high = mid
            elif isBadVersion(mid) == False: low = mid + 1
        return low
