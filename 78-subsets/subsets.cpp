class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> v;

        generatePowSet(nums, 0, {}, v);
        return v;
    }

    void generatePowSet(vector<int> &nums, int indx, vector<int> sub, vector<vector<int>> &v) {
        if(indx == nums.size()) {
            v.push_back(sub);
            return;
        }

        generatePowSet(nums, indx+1, sub, v);

        sub.push_back(nums[indx]);
        generatePowSet(nums, indx+1, sub, v);
    }
};