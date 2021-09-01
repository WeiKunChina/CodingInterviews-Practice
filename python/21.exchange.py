class Solution(object):
    """
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
    思路：
        首先指定前指针 start 和后指针 end，然后前指针定位偶数，后指针定位奇数，定位到之后将两个值互换，直到数组遍历完成
        时间复杂度：O(n)，空间复杂度：O(1)
    """
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] % 2 == 1:
                start += 1
            elif nums[end] % 2 == 0:
                end -= 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
        return nums