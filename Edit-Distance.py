class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        cache = [[float("inf")] * (m + 1) for i in range(n + 1)]

        for i in range(m + 1):
            cache[n][i] = m - i
        for j in range(n + 1):
            cache[j][m] = n - j

        for row in range(n - 1, -1, -1):
            for col in range(m - 1, -1, -1):
                if word1[row] == word2[col]:
                    cache[row][col] = cache[row + 1][col + 1]
                else:
                    cache[row][col] = 1 + min(
                        cache[row + 1][col],
                        cache[row][col + 1],
                        cache[row + 1][col + 1]
                        )
        return cache[0][0]
        
