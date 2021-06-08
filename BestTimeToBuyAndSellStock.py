#LC121: You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#Input: prices = [7,1,5,3,6,4]
#Output: 5

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        
        minSofar = prices[0]
        result = 0
        for p in prices[1:]:
            result = max(result, p-minSofar)
            minSofar = min(minSofar, p)
            
        return result
        
