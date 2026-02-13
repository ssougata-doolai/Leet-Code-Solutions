class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        // int max_l = 0, n = s.size(), j;
        // for(int i = 0; i < n; i++) {
        //     unordered_set<int> set;
        //     for(j = i; j < n; j++) {
        //         if(set.find(s[j]) != set.end()) break;
        //         set.insert(s[j]);
        //     }
        //     max_l = max(max_l, (int)set.size());
        // }

        // return max_l;

        int l = 0, r = 0, n = s.size(), res = 0;
        unordered_set<int> set;
        while(r < n) {
            while(set.find(s[r]) != set.end()) {
                set.erase(s[l]);
                l++;
            }
            set.insert(s[r++]);
            res = max(res, r-l);
        }
        return res;
    }
};