class Solution {
    public int maxProfit(int[] prices) {
        int min = prices[0];
        int max = -1;
        
        if (prices == null || prices.length == 0)
            return 0;
        
        for(int i = 0;i<prices.length;i++){
            int money = prices[i] - min;
            if(money > max) 
                max = money;
            if(prices[i] < min) 
                min = prices[i];
        }
        
        return max;
    }
}