class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        map = {}

        for n in range(len(numbers)):
            map[target - numbers[n]] = n+1
        
        print(map)

        for n in range(len(numbers)):
            if numbers[n] in map:
                return [n+1, map[numbers[n]]]
