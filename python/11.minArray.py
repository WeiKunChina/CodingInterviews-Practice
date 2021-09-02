class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        answer = numbers[0]
        start, end = 0, len(numbers) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if numbers[start] < numbers[mid]:
                start = mid
            elif numbers[start] > numbers[mid]:
                end = mid
            else:
                start += 1
                answer = min(answer, numbers[start])
        return min(answer, numbers[start], numbers[end])
