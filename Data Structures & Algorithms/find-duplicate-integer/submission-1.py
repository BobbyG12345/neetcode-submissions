class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == a:
                return a
            else:
                a = nums[i]