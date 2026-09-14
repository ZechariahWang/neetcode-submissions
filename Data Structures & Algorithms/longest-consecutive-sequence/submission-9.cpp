class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // approach: use a set [100,4,200,1,3,2]
        // filter out duplicates [100,4,200,1,3,2]
        // start looping through the entire set starting from the 1st index element [100, 4, 200, 1, 3, 2]
        // we are looking for any potential candidates for the start of a sequence
        // if n-1 does not exist inside the list, then this is a start of a potential valid sequence
        // run a while loop while n+1 exists inside the set
        // through each iteration, increase the count of the currentseq by 1, through each iteration also update longestSeq
        // if n+1 doesnt exist inside the set, break out and continue with the next potential candidate
        // at the very end, return longestSeq

        unordered_set<int> set(nums.begin(), nums.end());
        int longest_seq = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (!set.count(nums[i]-1)) {
                int current_seq = 1;
                int current_num = nums[i];
                while (set.count(current_num+1)) {
                    current_seq++;
                    current_num++;
                }
                if (current_seq > longest_seq) {
                    longest_seq = current_seq;
                }
            }

        }

        return longest_seq;
        
    }
};