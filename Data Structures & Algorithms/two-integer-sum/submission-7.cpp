class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // aproach: use a hashmap (key = )
        // loop through every number inside nums
        // make a var diff = target - num
        unordered_map<int, int> hashmap;
        for (int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];
            if (hashmap.count(diff)) {
                return {hashmap[diff], i};
            }
            hashmap[nums[i]] = i;

        }

        return {};
        
    }
};