class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l, r = i+1, len(nums)-1
            
            while l < r:
                if nums[l] + nums[r] == target:
                    triplets.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1 
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1

        return triplets
        