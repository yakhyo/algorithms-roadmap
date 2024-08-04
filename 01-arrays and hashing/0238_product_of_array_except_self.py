class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = []
        suffix_prod = []
        left, right = 1, 1
        for l, r in zip(nums, nums[::-1]):
            prefix_prod.append(left)
            left *= l

            suffix_prod.append(right)
            right *= r
        
        res = []
        for a, b in zip(prefix_prod, suffix_prod[::-1]):
            res.append(a * b)
        return res
        