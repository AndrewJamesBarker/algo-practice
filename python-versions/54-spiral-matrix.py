class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
      r,  c = len(matrix), len(matrix[0])
      ans = []
      top_wall, right_wall, bottom_wall, left_wall = 0, c, r, -1
      RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
      direction = RIGHT
      i, j = 0, 0
      while len(ans) != r * c:
          if direction == RIGHT:
              while j < right_wall:
                  ans.append(matrix[i][j])
                  j += 1
              i, j = i+1, j-1
              right_wall -= 1
              direction = DOWN
          elif direction == DOWN:
              while i < bottom_wall:
                  ans.append(matrix[i][j])
                  i += 1
              i, j = i-1, j-1
              bottom_wall -= 1
              direction = LEFT
          elif direction == LEFT:
              while j > left_wall:
                  ans.append(matrix[i][j])
                  j -= 1
              i, j = i-1, j+1
              left_wall += 1
              direction = UP
          else:
              while i > top_wall:
                  ans.append(matrix[i][j])
                  i -= 1
              i, j = i+1, j+1
              top_wall += 1
              direction = RIGHT

      return ans
    
print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
         

        

      
      
  