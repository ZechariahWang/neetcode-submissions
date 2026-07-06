class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {
        // move characters of t into a set
        // start from left side and search for first character in t
        // set that as left
        // keep track of what characters are in the substring with an array [loc, char]
        // keep going until you have a subtring containing all characters of t
        // at this point, keep going and put new characters that are in t in a set
        // after every time, check if it would be better to get rid of first element in array, and add all the new characters
        if (s.length === 0 || t.length === 0) return "";


        const tSet = new Set(t.split(''));
        // [index, character of t]
        const substringValues = [];
        // char => index
        const substringValuesMap = new Set();
        // any values after substringValues is filled
        let newValues = [];
        const newValuesMap = new Set();

        for (let i = 0; i < s.length; i ++) {
            if (tSet.has(s[i])) {
                if (substringValuesMap.size !== tSet.size) {
                    substringValues.push([i, s[i]]);
                    substringValuesMap.add(s[i]);
                }
                else {
                    newValues.push([i, s[i]]);
                    newValuesMap.add(s[i]);
                    console.log(substringValues, newValues);

                    let newStartingIndex = -1;
                    let removeIndex = -1;
                    for (let i = 0; i < substringValues.length; i ++) {
                        const substringValue = substringValues[i];
                        if (!newValuesMap.has(substringValues[1])) {
                            newStartingIndex = substringValue[0];
                            removeIndex = i;
                        }
                    }
                    if (newStartingIndex - substringValues[0][0] >= newValues[newValues.length - 1][0] - substringValues[substringValues.length - 1][0]) {
                        substringValues.splice(0, removeIndex - 1);
                        substringValues.push.apply(substringValues, newValues);
                        newValues = [];
                        newValuesMap.clear();
                    }
                }
            }
        }
        if (substringValuesMap.size !== tSet.size) {
            return "";
        }
        return s.substring(substringValues[0][0], substringValues[substringValues.length - 1][0] + 1);
    }
}
