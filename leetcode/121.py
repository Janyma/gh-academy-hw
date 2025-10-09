#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


def maxProfit( prices):
        profit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                day= prices[i]
                selling=prices[j]
                
                k=selling-day
                profit=max(profit, k)
                
        return profit
print(maxProfit([2,3,1,7]))

        