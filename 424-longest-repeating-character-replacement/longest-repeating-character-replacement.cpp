class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> freq(26, 0);
        int maxFreq = 0, left = 0, maxLen = 0, right;

        for(right = 0; right < s.size(); right++) {
            freq[s[right] - 'A']++;
            maxFreq = max(freq[s[right] - 'A'], maxFreq);

            while((right - left + 1) - maxFreq > k) {
                freq[s[left] - 'A']--;
                left++;
            }

            maxLen = max(maxLen, right-left+1);
        }

        return maxLen;

    }
};