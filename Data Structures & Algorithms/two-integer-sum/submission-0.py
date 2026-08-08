class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        container = {}
        for i , n in enumerate(nums):
            if target - n in container:
                return [container[target - n], i]
            container[n] = i