# Q1
# Leetcode 74. search a 2D Matrix

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: [0,1]


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: [-1,-1]

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

# O(n^2)
def searchMatrix(matrix, target): 

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == target:
        return [i, j]

  return [-1, -1]

def depthSearch(matrix, target):
  
  for i, val in enumerate(matrix):
    if val[0] == target:
      return [0, i]

    if val[0] <= target <= val[-1]:
      for j in range(len(val)):
        if val[j] == target:
          return [i, j]

  return [-1, -1]

# O(logn * logm)

# mid = len(matrix[row]) // 2
#
# if mid value is target:
#   return matrix index
#
# if mid 


    




matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target))
print(depthSearch(matrix, target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(searchMatrix(matrix, target))
print(depthSearch(matrix, target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 20
print(searchMatrix(matrix, target))
print(depthSearch(matrix, target))
