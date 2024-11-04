class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n = len(text1)
        m = len(text2)

        #Creating and populating DP array
        dp = [[0 for i in range(m + 1)] for i in range(n + 1)]

        #Traversing in reverse Order
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        #Selecting the first element
        return dp[0][0]
