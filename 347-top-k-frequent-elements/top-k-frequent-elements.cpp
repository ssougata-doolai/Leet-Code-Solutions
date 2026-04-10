class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mpp;
        vector<int> res;
        vector<pair<int, int>> count;

        for(int num : nums) {
            mpp[num]++;
        }
        for(auto &pair : mpp) {
            count.push_back({pair.second, pair.first});
        }
        sort(count.rbegin(), count.rend());
        for(int i = 0; i < k; i++) {
            res.push_back(count[i].second);
        }
        return res;
    }
};