class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for i,num in enumerate(nums):
            if num not in frequency:
                frequency[num] = 0
            frequency[num] += 1

        # Sort the items of the dictionary by value (frequency) in descending order
        sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        
        # Return the first k keys from the sorted list
        return [item[0] for item in sorted_items[:k]]
