class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // approach: run a prefix and suffix sum
        // make a prefix sum arr
        // loop through all numbers inside nums
        // do one forward pass multiple the current number in iteration by all numbers in front of it, store it inside the prefix sum
        // make a suffix array
        // loop through all numbers inside nums again but this time starting from the back
        // same logic, but multiply current num by all numbers behind it add result to suffix vector
        // at the very end, multiply all numbers in prefix verctor b suffix vector, append to sum vector
        // IN THEORY YOU SHOULDNT NEED PREFIX OR SUFFIX ARRAY
        // return res

        vector<int> res(nums.size());

        vector<int> prefixes(nums.size(), 1);
        int prefix = 1;
        for (int i = 0; i < nums.size(); i++) {
            prefixes[i] = prefix;
            prefix *= nums[i];
        }

        vector<int> suffixes(nums.size(), 1);
        int suffix = 1;
        for (int i = nums.size()-1; i >= 0; i--) {
            suffixes[i] = suffix;
            suffix *= nums[i];
            res[i] = suffixes[i] * prefixes[i];
        }

        return res;
        
    }
};