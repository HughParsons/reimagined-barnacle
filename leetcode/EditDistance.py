class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        dp[i][j] = min(
            dp[i+1][j+1] + cost(i,j), # replace
            dp[i+1][j] + 1, # delete
            dp[i][j-1] + 1, # insert
        )
        """
        n, m = len(word1), len(word2)
        
        @cache
        def rec(i, j):
            if i == n:
                return m - j 
            if j == m:
                return n - i 
                
            
            if word1[i] == word2[j]:
                return rec(i+1,j+1)
            
            else:
                return min(
                    1 + rec(i+1,j+1),
                    1 + rec(i+1, j),
                    1 + rec(i, j+1)
                )
        
        return rec(0,0)
