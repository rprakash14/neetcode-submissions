class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        out = []
        if 0 not in nums:

            product = 1
            for num in nums:
                product*=num
            
            for num in nums:
                out.append(product//num)
        
        elif nums.count(0) >= 2:
            return [0] * len(nums)

        else:
            product = 1;
            for num in nums:
                if num != 0:
                    product*=num
            for num in nums:
                if num != 0:
                    out.append(0)
                else:
                    out.append(product)
        return out

        
