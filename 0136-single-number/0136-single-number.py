class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0 # xor with zero. zero does not change xor result.
        
        for number in nums:
            result = number ^ result # xor with number
        
        return result