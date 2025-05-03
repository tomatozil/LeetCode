class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = []
        left, right = 0, len(nums)-1
        total = 1
        while left < right:
            if nums[left] == 0:
                zero.append(left)
            else:
                total *= nums[left]
            if nums[right] == 0:
                zero.append(right)
            else:
                total *= nums[right]
            left += 1
            right -= 1
        
        if left == right:
            if nums[left] == 0:
                zero.append(left)
            else:
                total *= nums[left]
        
        if zero:
            ret = [0] * len(nums)
            if len(zero) > 1 or len(zero) == len(nums):
                return ret
            for z in zero:
                ret[z] = total
            return ret
        else:
            return [total // x for x in nums]  