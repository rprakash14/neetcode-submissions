class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        fix = 0
        first = fix+1
        last = len(nums) - 1
        result = []

        for fix in range(len(nums)-2):
            if nums[fix] > 0:
                break
            
            if fix > 0 and nums[fix] == nums[fix-1]:
                continue
            
            first = fix + 1
            last = len(nums)-1

            while first < last:
                total = nums[fix] + nums[first] + nums[last]
            
                if total < 0:
                    first+=1
                elif total > 0:
                    last-=1 
                else:
                    result.append([nums[fix], nums[first], nums[last]])
                    first+=1
                    last-=1
            

                    while first < last and nums[first] == nums[first-1]:
                        first+=1
                
                    while first < last and nums[last] == nums[last+1]:
                        last-=1
        return result
                    