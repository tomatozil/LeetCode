import heapq

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_heap = [(-price, idx) for idx, price in enumerate(prices)]
        heapq.heapify(max_heap)

        min_price = float('inf')
        max_profit = 0

        while max_heap:
            neg_price, sell_idx = heapq.heappop(max_heap)
            sell_price = -neg_price
            
            for i in range(sell_idx):
                min_price = min(min_price, prices[i])
            
            profit = sell_price - min_price
            max_profit = max(max_profit, profit)

        return max_profit