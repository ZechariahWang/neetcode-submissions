class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;

        while (l < r) {
            int m = (l + r) / 2;
            if (nums[m] > nums[r]) {
                l = m + 1;
            } else if (nums[m] < nums[r]) {
                r = m;
            }
        }

        int pivot = l;
        l = 0;
        r = nums.size() - 1;

        if (target >= nums[pivot] && target <= nums[nums.size()-1]) {
            l = pivot;
            r = nums.size()-1;
        } else {
            l = 0;
            r = pivot - 1;
        }

        while (l <= r) {
            int m = l + (r-l) / 2;
            if (nums[m] == target) {
                return m;
            } else if (nums[m] < target) {
                l = m+1;
            } else if (nums[m] > target) {
                r = m - 1;
            }
        }

        return -1;
        
    }
};