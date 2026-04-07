class Solution {
public:
    bool isAnagram(string s, string t) {
        int freq[26] = {};

        if(s.size() != t.size()) return false;

        for(int i = 0; i < s.size(); i++) {
            freq[s[i] - 'a'] += 1;
            freq[t[i] - 'a'] -= 1;
        }

        for(auto item : freq) {
            if(item != 0) return false;
        }

        return true;
    }
};