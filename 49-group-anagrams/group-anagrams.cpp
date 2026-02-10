class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // unordered_map<string, vector<string>> mpp;
        // vector<vector<string>> res;

        // for(string &s : strs) {
        //     string sortedS = s;
        //     sort(sortedS.begin(), sortedS.end());
        //     mpp[sortedS].push_back(s);
        // }

        // for(auto pair : mpp) {
        //     res.push_back(pair.second);
        // }

        // return res;

        unordered_map<string, vector<string>> mpp;
        vector<vector<string>> result;

        for(string s : strs) {
            vector<int> count(26, 0);
            for(char c : s) {
                count[c - 'a'] += 1;
            }

            string key = "";
            for(int i : count) {
                key += to_string(i) + "#";
            }

            mpp[key].push_back(s);
        }

        for(auto pair : mpp) {
            cout << pair.first << " : ";
            for (const auto &word : pair.second) {
                cout << word << " ";
            }
            cout << endl;
            result.push_back(pair.second);
        }

        return result;
    }
};