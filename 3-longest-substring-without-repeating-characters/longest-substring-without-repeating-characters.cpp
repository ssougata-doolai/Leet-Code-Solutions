class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> seen;
        int maxL = 0, l = 0, r = 0;
        while(r < s.size()) {
            while(seen.find(s[r]) != seen.end()) {
                seen.erase(s[l]);
                l++;
            }
            seen.insert(s[r]);
            maxL = max(maxL, (r - l + 1));
            r++;
        }

        return maxL;
    }
};