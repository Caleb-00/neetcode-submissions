class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_array=[]

        for p in range(len(prices)):
            for i in range (p+1,len(prices)):
                profit=prices[i]-prices[p]
                profit_array.append(profit)

        if len(profit_array)==0:
            return 0
        return max(0,max(profit_array))


            