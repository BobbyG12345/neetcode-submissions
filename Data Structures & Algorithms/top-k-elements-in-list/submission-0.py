class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            d[num] += 1
        
        sorted_items = sorted(d.items(),key = lambda x:x[1],reverse=True)
        return [num for num,count in sorted_items[:k]]