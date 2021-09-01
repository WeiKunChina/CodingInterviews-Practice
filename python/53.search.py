class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1 and target == nums[0]:
            return 1
        if len(nums) == 1 and target != nums[0]:
            return 0
        # 找左边边界
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] >= target:
                right = middle
            else:
                left = middle + 1
        if nums[left] != target:
            return 0
        start = left

        # 找右边界
        if left == len(nums) - 1:
            return 1
        elif nums[left] != nums[left + 1]:
            return 1
        else:
            right = len(nums) - 1
            while left < right:
                middle = (left + right + 1) // 2
                if nums[middle] <= target:
                    left = middle
                else:
                    right = middle - 1
            return right - start + 1
