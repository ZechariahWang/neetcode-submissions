class Solution {
public:
    bool isAnagram(string s, string t) {
        // make two dictionaries, one for string s one for t
        // check if the length of s == t, if its not then its definitely not a valid anagram anyways, return false
        // loop through every character in string s
        // add it to the s dictionary (key maps to the character, value maps to the amount of times it occurs)
        // do the same thing for t
        // at the very end, do a comparsion of the dictionary s is equal to the dictionary t, and return that

        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char, int> s_map;
        unordered_map<char, int> t_map;
        
        for (int i = 0; i < s.length(); i++) {
            s_map[s[i]]++;
        }

        for (int i = 0; i < t.length(); i++) {
            t_map[t[i]]++;
        }

        return (s_map == t_map);
        
    }
};