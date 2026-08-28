class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=float('inf')
        profit=0
        for price in prices:
            minPrice=min(price,minPrice)
            profit=max(price-minPrice,profit)
        return profit