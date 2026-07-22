class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        map = set(nums)
        longest = 0

        for n in nums:
            #check if start of seq
            if n-1 not in map:
                length = 0
                while (n+length) in map:
                    length+=1
                longest = max(length, longest)
        return longest


