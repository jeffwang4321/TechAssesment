# Q2
# Leetcode 168. Excel Sheet Column Title

# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# AZ -> 52
# ...
# BA ->  53

# 53 - 26 = 27
# 27 - 26 = 1 -> B
# ...
# 53 - 1 = 52
# ...
# 52 % 26 -> 0 -> A


 

# Example 1:

# Input: columnNumber = 1
# Output: ?

# Example 2:
# Input: columnNumber = 28
# Output: ?


# Example 3:
# Input: columnNumber = 701
# Output: ?
 

# Constraints:
# 1 <= columnNumber <= 231 - 1