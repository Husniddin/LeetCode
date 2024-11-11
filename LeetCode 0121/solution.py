class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) in [0, 1] :
            return 0
        
        if len(prices) == 2:
            if prices[0] > prices[1] or prices[0] == prices[1]:
                return 0
            else:
                return prices[1] - prices[0]

        max_profit = 0
        buy_price, sell_price = prices[0], prices[1]

        i, j = 0, 1
        while j < len(prices):
            buy_price = min(buy_price, prices[i])
            profit = prices[j] - buy_price

            if profit > max_profit:
                max_profit = profit

            i+=1
            j+=1

        return max_profit
        

# Test Cases

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))