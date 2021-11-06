class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        x = 0
        for n in nums:
            x ^= n
            
        rsb = x & (x - 1) ^ x
            
        temp = x
        for n in nums:
            if n & rsb:
                temp ^= n
                
        return [temp, x ^ temp]
        
