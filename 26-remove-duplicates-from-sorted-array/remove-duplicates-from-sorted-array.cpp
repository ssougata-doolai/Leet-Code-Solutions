class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int left=0, right;
        for(right = 0; right < nums.size(); right++) {
            if(nums[right] == nums[left]) {
                continue;
            }
            nums[++left] = nums[right];
        }
        return left+1;
    }
};