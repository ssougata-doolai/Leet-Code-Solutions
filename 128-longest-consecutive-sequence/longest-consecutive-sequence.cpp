class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 0) return 0;

        int count, max_count = 0;
        unordered_set<int> seen;
        for(int i : nums) {
            seen.insert(i);
        }
        for(int n : seen) {
            if(seen.find(n - 1) == seen.end()) {
                count = 1;
                while(seen.find(++n) != seen.end()) count++;
                max_count = max(max_count, count);
            }
            
        }
        return max_count;
    }
};