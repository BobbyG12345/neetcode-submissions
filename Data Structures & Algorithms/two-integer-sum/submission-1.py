
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):

            otherNum = target - num

            for j, other in enumerate(nums):

                if i != j and other == otherNum:
                    return [i, j]