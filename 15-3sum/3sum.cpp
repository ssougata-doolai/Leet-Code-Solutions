class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        int n = nums.size(), l, r, s;
        sort(nums.begin(), nums.end());

        for(int i = 0; i < n; i++) {
            if(nums[i] > 0) break;
            if(i > 0 && nums[i] == nums[i-1]) continue;
            
            l = i + 1;
            r = n - 1;
            while(l < r) {
                s = nums[i] + nums[l] + nums[r];
                if(s == 0) {
                    res.push_back({nums[i], nums[l], nums[r]});
                    l++;
                    r--;
                    while(l < r && nums[l] == nums[l-1]) l++;
                    while(l < r && nums[r] == nums[r+1]) r--;
                }
                else if(s > 0) {
                    r--;
                }
                else {
                    l++;
                }
            }

        }
        return res;
    }
};