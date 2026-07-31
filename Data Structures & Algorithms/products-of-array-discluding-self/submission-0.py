class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product_res = 1
        for num in nums:
            product_res = num * product_res
        if product_res !=0:
            for i in range(len(nums)):
                res.append(int(product_res / nums[i]))
            return res
        else:
            product_res1 = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    res.append(0)
                else:
                    for j in range(len(nums)):
                        if j != i:
                            product_res1 = product_res1 * nums[j]
                    res.append(product_res1)
            return res   