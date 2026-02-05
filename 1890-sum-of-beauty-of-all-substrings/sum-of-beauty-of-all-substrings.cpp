class Solution {
public:
    int beautySum(string s) {
        
        int i, j, n=s.size(), sum=0, mini, maxi;

        for(i = 0; i < n; i++) {
            unordered_map<char, int> mpp;
            for(j = i; j < n; j++) {
                mpp[s[j]]++;
                mini = INT_MAX;
                maxi = INT_MIN;

                for(auto item : mpp) {
                    mini = min(mini, item.second);
                    maxi = max(maxi, item.second);
                }

                sum += (maxi - mini);
            }
        }
        return sum;
    }
};