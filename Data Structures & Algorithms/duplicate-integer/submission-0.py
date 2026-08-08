class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        element = {}
        for i,n in enumerate(nums):
            if n not in element:
                element[n] = i
            elif n in element:
                return True
        return False