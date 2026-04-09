class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mpp;
        vector<vector<string>> res;

        for(auto &s : strs) {
            vector<int> count(26, 0);
            for(char c : s) {
                count[c - 'a'] += 1;
            }
            
            string s1 = to_string(count[0]);
            for(int i = 1; i < 26; i++) {
                s1 += ',' + to_string(count[i]);
            }
            // cout<< s <<" : " << s1 << endl;
            mpp[s1].push_back(s);
        }
        for(auto &item : mpp) {
            res.push_back(item.second);
        }
        return res;
    }
};