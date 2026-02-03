class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int left = 0;
        for(int x : nums) {
            if(x != 0) {
                nums[left++] = x;
            }
        }
        while(left < nums.size()) {
            nums[left++] = 0;
        }
    }
};