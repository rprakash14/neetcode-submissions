class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash = {}

        for i in range(len(nums)):
            hash[target - nums[i]] = i


        for i in range(len(nums)):
            if nums[i] in hash and i != hash.get(nums[i]):
                return [i, hash.get(nums[i])]
