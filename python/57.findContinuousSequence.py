class Solution(object):
    def findContinuousSequence(self, target):
        """
        滑动窗口：
            设立左右指针，从开始位置维护一个子数组作为窗口，判断该窗口是否求和为 target， 如果是则将结果加入，如果小于 target 则窗口右移，大于 target 则窗口左移
            求和方式可以参考等差数列前n项和：S = n(a1+an)/2
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if target < 2:
            return [[1]]
        left, right = 1, 2
        while right <= (target // 2) + 1:
            s = (right - left + 1) * (left + right) / 2
            if s < target:
                right += 1
            elif s > target:
                left += 1
            else:
                element = []
                for i in range(left, right + 1):
                    element.append(i)
                result.append(element)
                # 千万别忘记，否则死循环
                left += 1
        return result
