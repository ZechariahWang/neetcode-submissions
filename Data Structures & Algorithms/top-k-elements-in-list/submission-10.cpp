class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // approach: 
        // make a count dictionary which stores the occurance of a certain element, key stores the number, value stores the number of times that number occurs
        // make a freq list with data types of lists, index is the occurance, the list is all numbers that occur that amount of times
        // first populate the count dictionary
        // then populate the frequency list
        // loop through the freq list from reverse since the highest index means those numbers occur the most
        // loop through all numbers in the list indexed last, going backwards through each iteration
        // append that number to a res list
        // once res list == k, return the res list

        unordered_map<int, int> count;
        vector<vector<int>> freq(nums.size() + 1);

        for (int i = 0; i < nums.size(); i++) { count[nums[i]]++; }
        for (auto [n, c] : count) { freq[c].push_back(n); }

        vector<int> res;
        for (int i = nums.size(); i > -1; i--) {
            for (auto n : freq[i]) {
                if (res.size() == k) {
                    return res;
                }
                res.push_back(n);
            }
        }

        return res;




    }
};