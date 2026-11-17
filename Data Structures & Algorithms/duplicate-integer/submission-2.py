class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for each in nums:
            if each in freq:
                return True
                break
            freq[each]=1
        return False
            
            
        