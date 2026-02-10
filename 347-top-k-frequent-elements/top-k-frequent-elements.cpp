class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for(int &n : nums) {
            count[n]++;
        }

        vector<pair<int, int>> freq;
        for(auto &c: count) {
            freq.push_back({c.second, c.first});
        }

        sort(freq.begin(), freq.end());

        int indx = 0;
        vector<int> res;

        for(int i = freq.size()-1; i >=0 ; i--) {
            res.push_back(freq[i].second);
            if(++indx == k) break;
        }
        return res;
    }
};