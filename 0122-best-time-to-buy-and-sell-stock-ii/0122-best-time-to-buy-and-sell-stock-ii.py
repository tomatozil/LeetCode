class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start = 0
        while start < len(prices):
            cur = start
            next = cur + 1
            while cur < next:
                if next >= len(prices):
                    break
                if prices[cur] > prices[next]:
                    break
                cur += 1
                next += 1
            end = cur
            if start != end:
                profit += prices[end] - prices[start]
            start = next
        
        return profit
