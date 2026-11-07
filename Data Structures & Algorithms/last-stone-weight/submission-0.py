class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            if len(stones) == 1:
                return stones[0]
            elif stones:
                stones_sort = sorted(stones)
                new_stone= stones_sort[-1] - stones_sort[-2]
                stones.remove(stones_sort[-1])
                stones.remove(stones_sort[-2])
                stones.append(new_stone)
            else:
                return 0
            
            

             
        