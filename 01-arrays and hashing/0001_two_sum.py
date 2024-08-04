# solution 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i, num in enumerate(nums):
            if target-num in freq:
                return [freq[target-num], i]
            freq[num] = i
        
# solution 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        