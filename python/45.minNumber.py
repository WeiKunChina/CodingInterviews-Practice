import functools
class Solution(object):
    """
    拼接数组内所有元素使结果最小，本质上是排序
    若字符串拼接 a + b > b + a，那么排序上 b < a;
    根据这个规则对数组内的元素排序
    时间复杂度：O(nlog_n)。 n 为 strList 列表长度
    """

    def minNumber(self, nums):
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(strs)
