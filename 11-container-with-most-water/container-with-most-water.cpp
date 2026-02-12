class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_water = 0, water, n = height.size();
        int l = 0, r = height.size()-1;
        while(l < r) {
            max_water = max(max_water, ((r - l) * min(height[l], height[r])));
            if(height[l] <= height[r]) l++;
            else r--;
        }
        return max_water;
    }
};