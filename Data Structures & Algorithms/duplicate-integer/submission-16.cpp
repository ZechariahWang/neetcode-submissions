class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // approach: make a set
        // for every number in the vector, check if its in the set
        // if it is, then its a duplicate, return True 
        // otherwise, add that number to the set
        // at the very end, return False if none of the other conditions have been met
        unordered_set<int> seen;
        for (int i = 0; i < nums.size(); i++){
            if (seen.count(nums[i])) { 
                return true;
            }
            seen.insert(nums[i]);
        }

        return false;
        
    }
};