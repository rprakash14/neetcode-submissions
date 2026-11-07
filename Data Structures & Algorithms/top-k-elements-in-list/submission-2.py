class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            
            else: 
                frequency[num] = 1
        
        heap = []
        heapq.heapify(heap)

        for key in frequency:
            heapq.heappush(heap, (frequency[key], key))
        
        
        output = []

        print(len(heap))

        while len(heap) > k:
            heapq.heappop(heap)
        
        for i in heap:
            output.append(i[1])
        
        return output
        