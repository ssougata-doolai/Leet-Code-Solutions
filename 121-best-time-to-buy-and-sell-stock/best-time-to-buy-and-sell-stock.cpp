class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_p = 0, n = prices.size(), j, min_price = INT_MAX;
        for(int i = 0; i < n; i++) {
            min_price = min(min_price, prices[i]);
            max_p = max(max_p, prices[i] - min_price);
        }

        return max_p;
    }
};