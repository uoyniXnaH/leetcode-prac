var lengthOfLongestSubstring = function(s) {
    let ans = "";
    let hold = "";
    let pos = 0;
    for (i = 0; i < s.length; i++) {
        // console.log(`hold: ${hold}, ans: ${ans}`);
        if (hold.includes(s[i])) {
            pos = hold.indexOf(s[i]);
            if (hold.length > ans.length) {
                ans = hold;
            }
            hold = hold.slice(pos + 1) + s[i];
        } else {
            hold += s[i];
        }
    }
    if (hold.length > ans.length) {
        ans = hold;
    }
    return ans.length;
};