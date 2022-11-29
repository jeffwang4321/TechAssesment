# Q1
# Leetcode 74. search a 2D Matrix

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 // [1,3,5,7,10,11,16,20,23,30,34,60]
# Output: [0,1]


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: [-1,-1]

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

# O(n + logm) < O(m*n) n = rows, m = cols

class Solution {
    public static int[] matrixSearch(int[][] arr, int target){
        if(arr.length == 0 || arr[0].length == 0){
            return new int[]{-1, -1};
        }

        int currRow = 0; # 1

        while(arr[currRow][0] <= target){
            currRow += 1;
        }

        int focusRow = currRow - 1; # 0 

        # [1,3,5,7]
        int searchIndex = binSearch(arr[focusRow], 0, arr[focusRow].length, target);

        if(searchIndex != -1){
            return new int[]{focusRow, searchIndex}

            # [0, 1]
        }

        return new int[]{-1, -1};
    } 

    public static int binSearch(int[] arr, int left, int right, int target){
        if(right <= left){
            return -1;
        }

        # l = 0
        # r = 3


        while(right >= left){
            int mid = left + (right - left)/2;

            # 1

            if(arr[mid] == target){
                return mid;
            } else if(arr[mid] > target){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return -1;
    }


    public static void main(String[] args){

    }

}