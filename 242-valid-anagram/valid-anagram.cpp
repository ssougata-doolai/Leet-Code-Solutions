class Solution {
public:
    bool isAnagram(string s, string t) {
        int freq[26] = {};

        if(s.size() != t.size()) return false;

        for(auto ch : s) {
            freq[ch - 'a'] += 1;
        }
        
        for(auto ch : t) {
            freq[ch - 'a'] -= 1;
        }

        for(auto item : freq) {
            if(item != 0) return false;
        }

        return true;
    }
};