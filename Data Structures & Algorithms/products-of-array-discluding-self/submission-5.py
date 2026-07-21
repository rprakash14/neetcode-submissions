class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0

        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                product *= n

        out = [0] * len(nums)

        for i in range(len(nums)):
            if zero_count > 1:
                out[i] = 0
            elif zero_count == 1:
                if nums[i] == 0:
                    out[i] = product
                else:
                    out[i] = 0
            else:
                out[i] = product // nums[i]

        return out