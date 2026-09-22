class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // approach: prefix and suffix sum
        // prefixes = []
        // prefix = 1

        vector<int> res(nums.size());

        vector<int> prefixes(nums.size(), 1);
        int prefix = 1;
        for (int i = 0; i < nums.size(); i++) {
            prefixes[i] = prefix;
            prefix *= nums[i];
        }

        vector<int> suffixes(nums.size(), 1);
        int suffix = 1;
        for (int i = nums.size()-1; i >-1; i--) {
            suffixes[i] = suffix;
            suffix *= nums[i];
            res[i] = suffixes[i] * prefixes[i];
        }

        return res;

    }
};