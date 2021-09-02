class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_value, max_value, zero_count = 0, 0, 0
        d = {}
        for index in range(len(nums)):
            if nums[index] == 0:
                zero_count += 1
                continue
            if nums[index] in d:
                return False
            if min_value == 0 and max_value == 0:
                min_value, max_value = nums[index], nums[index]
            min_value = min(nums[index], min_value)
            max_value = max(nums[index], max_value)
            d[nums[index]] = 1
        if zero_count > 2:
            return False
        return max_value - min_value < 5
