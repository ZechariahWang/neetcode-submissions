class Solution {
public:
    bool isPalindrome(string s) {
        // approach: use two pointers
        // declare a left pointer from the left side of the string
        // declare a right pointer from the right side of the string
        // do a while loop while l < r:
        // inside the while loop run two more while loops, one for each respective pointer
        // these loops run while l<r and the current character is not alphanumeric, bc we dont consider it part of the string
        // while this is the case, increase l and decrease r respectively 
        // once both loops run, do an if so that if l == r:, increase l and decrease r
        // if at any given point they are not equal, then this string isnt a palindrome, return false
        // otherwise if it makes it to the very end, return true since this is definitley a valid palindrome

        int l = 0;
        int r = s.size()-1;

        while (l < r) {
            while (l < r && !isalnum(s[l])) { l++; }
            while (l < r && !isalnum(s[r])) { r--; }

            if (tolower(s[l]) != tolower(s[r])) { return false; }
            l += 1;
            r -= 1;
        }

        return true;
        
    }
};