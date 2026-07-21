class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        A = []

        for i in range(len(nums)):
            A.append([nums[i], i])

        nums_sort = sorted(A)
        
        start=0
        end = len(nums)-1

        print(nums_sort)

        while start < end:
            sum = nums_sort[start][0] + nums_sort[end][0]
            if sum == target:
                return sorted([nums_sort[start][1], nums_sort[end][1]])
            elif sum < target:
                start+=1
            elif sum > target:
                end-=1