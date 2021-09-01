class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] != middle:
                right = middle
            else:
                left = middle + 1
        if left == nums[-1]:
            return left + 1
        else:
            return left
