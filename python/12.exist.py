class Solution(object):

    # 定义上下左右四个行走方向
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self, board, word):
        """
        题目可以模拟为 DFS 的过程，即从一个方向搜索到底，再回溯上一个节点，沿另一个方向继续搜索，递归进行。
        在搜索过程中，若遇到该路径不可能与目标字符串匹配的情况，执行剪枝，立即返回。
        时间复杂度：O(3^k IJ)。 一次搜索完全部矩阵的时间复杂度为 O(IJ) ，共需要 3^ 次搜索。
        空间复杂度：搜索过程中的递归深度不超过 KK ，因此系统因函数调用累计使用的栈空间占用 O(K)
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(self, board, word, i, j, k):
        """
        :param board: List[List[str]]
        :param word: str
        :param i: index
        :param j: index
        :param k: index
        :return: bool
        """
        if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        tmp = board[i][j]
        board[i][j] = '/'
        result = self.dfs(board, word, i + 1, j, k + 1) or \
                 self.dfs(board, word, i - 1, j, k + 1) or \
                 self.dfs(board, word, i, j + 1, k + 1) or \
                 self.dfs(board, word, i, j - 1, k + 1)
        board[i][j] = tmp
        return result
