class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // approach: make a default dict with a default value of list
        // loop through every single string in the strs list
        // make a count list, size of 26 representing the count of each character in the list
        // loop through every char in the individual string, increase the count of that char in the count var

        map<vector<int>, vector<string>> res;

        for (auto s : strs) {
            vector<int> count(26);
            for (auto c : s) {
                count[c-'a']++;
            }
            res[count].push_back(s);
        }

        vector<vector<string>> out;
        for (auto [key, group] : res) {
            out.push_back(group);
        }

        return out;
    }
};