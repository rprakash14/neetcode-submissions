import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        heap = [-g for g in gifts]
        heapq.heapify(heap)

        for i in range(k):
            pop = abs(heapq.heappop(heap))
            heapq.heappush(heap, -math.floor(math.sqrt(pop)))
            
        return -sum(heap)
        
        