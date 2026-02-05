class Solution {
public:
    bool isIsomorphic(string s, string t) {
        // unordered_map<char, char> mpp1, mpp2;

        // for(int i = 0; i < s.size(); i++) {
        //     if(mpp1.find(s[i]) != mpp1.end()) {
        //         if(mpp1[s[i]] != t[i]) return false;
        //     }
        //     else if(mpp2.find(t[i]) != mpp2.end()){
        //         return false;
        //     }
        //     mpp1[s[i]] = t[i];
        //     mpp2[t[i]] = s[i];
        // }

        int m1[256] = {0}, m2[256] = {0};

        for(int i = 0; i < s.size(); i++) {
            if(m1[s[i]] != m2[t[i]]) return false;

            m1[s[i]] = i+1;
            m2[t[i]] = i+1;
        }
        return true;
    }
};