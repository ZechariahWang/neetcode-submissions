class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // aproach run two pointers
        // make a res vector
        // sort the vector
        // run a for loop throughout the entire vector nums
        // if the current i val is the same as the i-1 val, continue
        // inside the for loop, run two pointers L, R
        // L = i + 1, R = size of nums - 1
        // do a check if current = nums[l] + nums[r] + nums[i] == 0
        // if it does then it is a valid set, insert it into the vector
        // l += 1, r -=1, afterwards continuously increase l while nums[l]==nums[l-1] to avoid duplicates
        // if current > 0, r -= 1
        // if current < 0, l += 1
        // at the end of the loop, outside return the res vector

        vector<vector<int>> res;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size()-1; i++) {
            if (i > 0 && nums[i]==nums[i-1]) { continue; }
            int l = i+1;
            int r = nums.size() - 1;
            while (l < r) {
                int current = nums[i]+nums[l]+nums[r];
                if (current == 0) {
                    res.push_back({nums[i], nums[l], nums[r]});
                    l++;
                    r--;
                    while (nums[l]==nums[l-1] && l < r) { l++; }
                }
                if (current > 0) { r -= 1; }
                if (current < 0) { l += 1; }
            }
        }

        return res;
        
    }
};