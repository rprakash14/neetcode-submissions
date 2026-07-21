class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, count in count.items():
            freq[count].append(num)
        
        out = []
        
        for i in range(len(freq)):
            for num in freq[len(freq) - 1 - i]:
                out.append(num)
                if len(out) == k:
                    return out
        
