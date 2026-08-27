
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            otherNum = target - num
            if otherNum in seen:
                return [seen[otherNum],i]
          
            seen[num]=i
        