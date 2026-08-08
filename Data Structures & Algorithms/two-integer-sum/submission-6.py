class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # container = {}
        # for i , n in enumerate(nums):
        #     if target - n in container:
        #         return [container[target - n], i]
        #     container[n] = i

        num_idx = [(n,i) for i,n in enumerate(nums)]
        num_idx.sort()
        left = 0
        right = len(num_idx)-1
        while left < right:
            sum = num_idx[left][0] + num_idx[right][0]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return sorted([num_idx[left][1], num_idx[right][1]])