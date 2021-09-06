import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return " "
        d = {}
        for element in s:
            if element in d:
                d[element] = False
            else:
                d[element] = True
        for c in s:
            if d[c]:
                return c
        return " "

    def firstUniqCharQueue(self, s):
        """
        :type s: str
        :rtype: str
        """
        position = {}
        deque = collections.deque([])
        for index, element in enumerate(s):
            if element not in position:
                position[element] = index
                deque.append((s[index], index))
            else:
                position[element] = -1
                # 循环删除队列头部不是第一次出现的元素
                while deque and position[deque[0][0]] == -1:
                    deque.popleft()
        if not deque:
            return ' '
        else:
            return deque[0][0]
