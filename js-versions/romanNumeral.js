/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
  const romNums = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000
  };

  let result = 0;
  for (let i = 0; i < s.length; i++) {
    let current = romNums[s[i]];
    let next = romNums[s[i + 1]];
    if (current < next) {
      result += next - current;
      i++;
    } else {
      result += current;
    }
  }    
  console.log(result); 

  return result; 
};

// Invoke the function to see the output
romanToInt("III"); // Example input
