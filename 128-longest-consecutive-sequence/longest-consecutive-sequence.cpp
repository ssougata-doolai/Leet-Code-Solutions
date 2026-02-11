class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int max_counter = 1, counter = 1;
        if(nums.size() == 0) return 0;
        for(int i = 1; i < nums.size(); i++) {
            if(nums[i-1] == nums[i]) continue;
            if(nums[i-1] - nums[i] == -1) {
                counter += 1;
                max_counter = max(max_counter, counter);
                continue;
            }
            counter = 1;
        }

        return max_counter;
    }
};