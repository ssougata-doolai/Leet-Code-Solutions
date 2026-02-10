class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // unordered_map<int, int> count;
        // for(int &n : nums) {
        //     count[n]++;
        // }

        // vector<pair<int, int>> freq;
        // for(auto &c: count) {
        //     freq.push_back({c.second, c.first});
        // }

        // sort(freq.begin(), freq.end());

        // int indx = 0;
        // vector<int> res;

        // for(int i = freq.size()-1; i >=0 ; i--) {
        //     res.push_back(freq[i].second);
        //     if(++indx == k) break;
        // }
        // return res;

        unordered_map<int, int> count; 
        vector<pair<int, int>> bucket;
        vector<int> res;
        int n=0;
        for(int &n : nums) {
            count[n]++;
        }
        
        for(auto &c : count) {
            bucket.push_back({c.second, c.first});
        }

        sort(bucket.begin(), bucket.end());

        for(int i = bucket.size()-1; i >=0; i--) {
            res.push_back(bucket[i].second);
            if(++n == k) break;
        }

        return res;
    }
};