class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_len = 0
        num_set = set(nums)

        for num in nums:
            if num - 1 not in num_set:
                curr = num
                curr_len = 1
                while curr + 1 in num_set:
                    curr += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len
