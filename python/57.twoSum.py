class Solution(object):
    def twoSumDict(self, nums, target):
        """
        用字典缓存, 加速查找，直接计算
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, element in enumerate(nums):
            if target - element in d:
                return [target - element, element]
            d[element] = i

    def twoSum(self, nums, target):
        """
        双指针思路：
            因为数组本身是有序的，那么完全可以在数组的开头 start 和结尾 end 位置各设置一个指针，通过二者的加和 sum 来找到目标值 target
            如果 sum < target，则 start++，这样可以让下一次的 sum 变大，如果 sum > target，则 end--，这样可以让下一次的 sum 变小
        时间复杂度：O(n)O(n)，空间复杂度：O(1)O(1)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] + nums[end] < target:
                start += 1
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                return [nums[start], nums[end]]
