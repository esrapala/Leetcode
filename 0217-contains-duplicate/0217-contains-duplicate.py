class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        '''
        hashSet = set()
        
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False
        '''