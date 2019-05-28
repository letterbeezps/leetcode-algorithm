/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = function(s) {
  let result = true;
  const left = ["(", "[", "{"];
  const right = [")", "]", "}"];
  const compare = [];
  Array.from(s).forEach((item, idx, array) => {
    if (left.includes(item)) {
      compare.push(right[left.indexOf(item)]);
    } else {
      let curr = compare.pop();
      if (curr !== item) {
        result = false;
      }
    }
  });
  if (compare.length > 0) {
    return false;
  }
  return result;
};
