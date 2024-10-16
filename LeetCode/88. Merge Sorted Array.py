class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1

        num1_pointer = m - 1
        num2_pointer = n - 1
        right_idx = m + n - 1

        while num2_pointer >= 0:
            if num1_pointer >=0 and nums1[num1_pointer] > nums2[num2_pointer]:
                nums1[right_idx] = nums1[num1_pointer]
                num1_pointer  = num1_pointer - 1
            else:
                nums1[right_idx] = nums2[num2_pointer]
                num2_pointer  = num2_pointer - 1

            right_idx = right_idx - 1
