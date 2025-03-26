class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums.sort()
        for i in range(len(nums)):
            target = -nums[i]
            l, r = i+1, len(nums)-1
            
            while l < r:
                if nums[l] + nums[r] == target:
                    new_list = sorted([nums[l], nums[r], nums[i]])
                    if new_list not in triplets:
                        triplets.append(new_list)
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1

        return triplets
        