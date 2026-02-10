class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mpp;
        int n = nums.size();

        for(int i = 0; i < n; i++) {
            if(mpp.find(nums[i]) != mpp.end()) {
                // cout<< nums[i] << ":" << mpp[nums[i]] << endl;
                return {mpp[nums[i]], i};
            }

            mpp[target - nums[i]] = i;
        }
        return {};
    }
};