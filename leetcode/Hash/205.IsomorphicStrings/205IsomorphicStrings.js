/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

var isIsomorphic$1 = function (s, t) {
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

var isIsomorphic$2 = function (s, t) {
    const s2t = {};
    const t2s = {};

    for (let index in s) {
        if (s.hasOwnProperty(index)) {
            const sEle = s[index];
            const tEle = t[index];
            if (s2t[sEle] == null) {
                s2t[sEle] = t[index];
            } else if (s2t[sEle] && s2t[sEle] !== tEle) {
                return false;
            }
            if (t2s[tEle] == null) {
                t2s[tEle] = s[index];
            } else if (t2s[tEle] && t2s[tEle] !== sEle) {
                return false;
            }
        }
    }

    return true;
};
