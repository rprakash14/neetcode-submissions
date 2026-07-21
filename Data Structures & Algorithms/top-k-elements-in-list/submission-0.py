class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}

        for i in nums:

            if i in map:
                map[i] += 1
            else: 
                map[i] = 0
        
        
        print(map)
        out = []
        while k > 0:
            key = next((k for k, v in map.items() if v == max(map.values())), None)
            out.append(key)
            del map[key]
            k -= 1
        
        return out



        

        