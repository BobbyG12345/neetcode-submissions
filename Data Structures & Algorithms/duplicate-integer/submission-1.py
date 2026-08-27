class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = set()
        for num in nums:
            if num not in m:
                m.add(num)
            else:
                return True
        return False