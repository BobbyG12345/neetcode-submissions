class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sorted_stones=sorted(stones)
        while len(sorted_stones) > 1:
            if sorted_stones[-1] == sorted_stones[-2]:
                del sorted_stones[-1]
                del sorted_stones[-1]
            elif sorted_stones[-1] < sorted_stones[-2]:
                sorted_stones[-2] = sorted_stones[-2]-sorted_stones[-1]
                del sorted_stones[-1]
                sorted_stones.sort()
            elif sorted_stones[-1] > sorted_stones[-2]:
                
                sorted_stones[-1] = sorted_stones[-1]-sorted_stones[-2]
                del sorted_stones[-2]
                sorted_stones.sort()
        if sorted_stones:
            return sorted_stones[0]
        else:
            return 0