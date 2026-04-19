class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.length() > s2.length()) {
            return false;
        }
        
        vector<int> freq1(26, 0), freq2(26, 0);
        int l = 0, r, matches = 0;
        for(int i = 0; i < s1.size(); i++) {
            freq1[s1[i] - 'a']++;
            freq2[s2[i] - 'a']++;
        }

        for(int i = 0; i < 26; i++) {
            if(freq1[i] == freq2[i]) {
                matches++;
            }
        }

        for(r = s1.size(); r < s2.size(); r++) {
            if(matches == 26) {
                return true;
            }

            int indx1 = s2[r] - 'a';
            freq2[indx1]++;
            if(freq1[indx1] == freq2[indx1]) {
                matches++;
            } else if(freq1[indx1] + 1 == freq2[indx1]) {
                matches--;
            }

            int indx2 = s2[l] - 'a';
            freq2[indx2]--;
            if(freq1[indx2] == freq2[indx2]) {
                matches++;
            } else if(freq1[indx2] - 1 == freq2[indx2]) {
                matches--;
            }
            
            l++;
        }
        
        return matches == 26;
    }
};