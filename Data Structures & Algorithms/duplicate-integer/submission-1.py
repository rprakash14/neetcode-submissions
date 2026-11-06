class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        set = {}

        for num in nums:
            if num in set:
                return True
            set[num] = ""
        
        return False
        