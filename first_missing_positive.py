# Leetcode #41: First Missing Positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n > 0:
                seen.add(n)
        m = 1
        while m in seen:
            m += 1
        return m