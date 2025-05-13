class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        house_robbed = [-1]*length
        
        def robbing(index) -> int:
            if index >= length:
                return 0
            if house_robbed[index] > -1:
                return house_robbed[index]

            nums[index] += max(robbing(index + 2), robbing(index + 3))
            house_robbed[index] = nums[index]

            return house_robbed[index]
        
        return max(robbing(0), robbing(1))