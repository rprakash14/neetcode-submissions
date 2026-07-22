class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        map = defaultdict(int)

        res = 0
        maxCount = 0
        for num in nums:
            map[num] +=1
            if maxCount < map[num]:
                res = num
                maxCount = map[num]
        
        return res