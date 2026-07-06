class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const numLetters = new Map(); // positive for letters in s, negative for t

        for (const letter of s) {
            numLetters.set(letter, (numLetters.get(letter) ?? 0) + 1);
        }
        for (const letter of t) {
            if (!numLetters.has(letter)) {
                return false;
            }
            numLetters.set(letter, numLetters.get(letter) - 1);
            if (numLetters.get(letter) <= 0) {
                numLetters.delete(letter);
            }
        }
        return numLetters.size() === 0;
    }
}
