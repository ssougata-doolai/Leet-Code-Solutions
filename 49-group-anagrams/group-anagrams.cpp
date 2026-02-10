class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mpp;
        vector<vector<string>> res;

        for(string &s : strs) {
            string sortedS = s;
            sort(sortedS.begin(), sortedS.end());
            mpp[sortedS].push_back(s);
        }

        for(auto pair : mpp) {
            res.push_back(pair.second);
        }

        return res;
    }
};