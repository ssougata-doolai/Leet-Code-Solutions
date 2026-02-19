class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int i, n = s2.size(), m = s1.size();
        string subs;
        sort(s1.begin(), s1.end());

        for(i = 0; i < n; i++) {
            subs = s2.substr(i, m);
            sort(subs.begin(), subs.end());

            if(s1 == subs) {
                return true;
            }
        }
        return false;
    }
};