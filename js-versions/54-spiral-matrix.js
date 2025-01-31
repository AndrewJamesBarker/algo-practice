/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
  const row = matrix.length; 
  const col = matrix[0].length;
  
  let i = 0, j = 0;  
  let right_wall = col, bottom_wall = row, left_wall = -1, top_wall = 0;
  const ans = [];
  const RIGHT = 0, DOWN = 1, LEFT = 2 , UP = 3;
  let direction = RIGHT;
  while (ans.length < row * col) {
      if (direction === RIGHT) {
          while (j < right_wall) {
              ans.push(matrix[i][j]);
              j += 1;
          }
          i += 1;
          j -= 1;
          right_wall -= 1;
          direction = DOWN;
      } else if (direction === DOWN) {
          while (i < bottom_wall) {
              ans.push(matrix[i][j]);
              i += 1;
          }
          i -= 1;
          j -= 1;
          bottom_wall -= 1;
          direction = LEFT
      } else if (direction === LEFT) {
          while (j > left_wall) {
              ans.push(matrix[i][j]);
              j -= 1;
          }
          i -= 1;
          j += 1;
          left_wall += 1;
          direction = UP
      } else {
          while (i > top_wall) {
              ans.push(matrix[i][j]);
              i -= 1;
          }
          i += 1;
          j += 1;
          top_wall += 1;
          direction = RIGHT
      }
  }
  return ans;
};

