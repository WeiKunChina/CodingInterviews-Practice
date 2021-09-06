import queue
import collections


class MaxQueue(object):

    def __init__(self):
        self.deque1 = collections.deque([])
        self.queue1 = queue.Queue()

    def max_value(self):
        """
        :rtype: int
        """
        if self.queue1 and len(self.deque1) > 0:
            return self.deque1[0]
        else:
            return -1

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        while self.deque1 and self.deque1[-1] < value:
            self.deque1.pop()
        self.deque1.append(value)
        self.queue1.put(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.deque1:
            return -1
        result = self.queue1.get()
        if result == self.deque1[0]:
            self.deque1.popleft()
        return result
