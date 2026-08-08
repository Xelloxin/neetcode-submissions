class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        container = {}
        for i , n in enumerate(nums):
            if target - n in container:
                return [container[target - n], i]
            container[n] = i
        # left = 0
        # right = len(nums)-1
        # while left < right:
        #     if nums[left] + nums[right] < target:
        #         left += 1
        #     elif nums[left] + nums[right] > target:
        #         right -= 1
        #     else:
        #         return [left,right]
         