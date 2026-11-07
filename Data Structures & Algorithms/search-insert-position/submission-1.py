class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1

        while start <= end:
            print(start)
            print(end)
            i = (start + end) // 2

            if nums[i] < target:
                start = i + 1
            
            elif nums[i] > target:
                end = i - 1
            
            elif nums[i] == target:
                return i 
        
        print('notfound')
        return start


            
