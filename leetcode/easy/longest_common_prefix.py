class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mxI = len(min(strs, key = len))
        ans = ""
        
        for i in range(mxI):
            candidate = strs[0][i]
            for s in strs:
                if s[i] != candidate:
                    return ans
            ans += candidate
            
        return ans
        
