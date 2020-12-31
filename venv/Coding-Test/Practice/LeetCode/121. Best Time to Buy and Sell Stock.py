# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    if len(prices) > 1 :
        profits = []
        for i in range(len(prices)-1) :
            buy = prices[i]
            sell = max(prices[i+1:])
            profit = sell-buy
            if profit < 0 :
                profit = 0
            profits.append(profit)
        answer = max(profits)
    else :
        answer = 0
    return answer


stock = [7, 1, 5, 3, 6, 4]
print(maxProfit(stock))