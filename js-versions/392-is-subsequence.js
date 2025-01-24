/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
  const S = s.length;
  const T = t.length
  if (s === "") {
      return true;
  }
  if (S > T) {
      return false;
  }
  let j = 0;
  for (let i = 0; i < T; i++) {
      if (t[i] === s[j]) {
          if (j === S - 1) {
              return true;
          } else {
              j++;
          }
      }
  }
  return false;
};