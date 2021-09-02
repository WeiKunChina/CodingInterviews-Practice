class CQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        # 1 -> 2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # add value
        self.stack1.append(value)
        # 1 <- 2
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return self.stack1

    def deleteHead(self):
        """
        :rtype: int
        """
        if not self.stack1:
            return -1
        return self.stack1.pop()
