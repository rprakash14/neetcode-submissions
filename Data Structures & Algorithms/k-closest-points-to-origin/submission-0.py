class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ##min heap on distance to origin 
        ## append distance and then index in og points list

        minHeap = []
        heapq.heapify(minHeap)

        for i, point in enumerate(points):
            distance = math.sqrt((point[0] - 0) ** 2 + (point[1] - 0) ** 2)
            heapq.heappush(minHeap, (distance, i))


        indices = []
        res = []

        for i in range(k):
            indices.append(heapq.heappop(minHeap)[1])

        print(indices)
        for i in indices:
            res.append(points[i])

        return res

        

            
            



