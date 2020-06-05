/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
    const s2t = {};
    const t2s = {};
    let result = true;
    [...s].forEach((char, index) => {
        if (s2t[char] == null) {
            s2t[char] = t[index];
        } else if (s2t[char] && s2t[char] !== t[index]) {
            result = false;
        }
    });
    [...t].forEach((char, index) => {
        if (t2s[char] == null) {
            t2s[char] = s[index];
        } else if (t2s[char] && t2s[char] !== s[index]) {
            result = false;
        }
    });

    return result;
};
