# PROBLEM:

# Write a function that reverses the order of the words in a string.
# For example, your function should transform the string “Do or do not, there is no try.”
# to “try. no is there not, do or Do”. Assume that all words are space delimited and
# treat punctuation the same as letters.

# Solution:

str = "Do or do not, there is no try."
str2 = str.split()[::-1]
print(id(str))
print(id(str2))
print(" ".join(str2))
