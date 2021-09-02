class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        if not a:
            return []
        result = [1] * len(a)
        forward_sum = [1] * len(a)
        back_sum = [1] * len(a)
        forward_sum[0] = a[0]
        back_sum[-1] = a[-1]
        for i in range(1, len(a)):
            forward_sum[i] = forward_sum[i - 1] * a[i]
            back_sum[len(a) - i - 1] = back_sum[len(a) - i] * a[len(a) - i - 1]
        for index in range(1, len(a) - 1):
            result[index] = forward_sum[index - 1] * back_sum[index + 1]
        result[0] = back_sum[1]
        result[len(a) - 1] = forward_sum[len(a) - 2]
        return result
