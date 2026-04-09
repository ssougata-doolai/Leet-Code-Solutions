class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mpp;
        vector<vector<string>> res;

        for(auto s : strs) {
            string s1 = s;
            sort(s1.begin(), s1.end());
            mpp[s1].push_back(s);
        }
        for(auto &item : mpp) {
            res.push_back(item.second);
        }
        return res;
    }
};