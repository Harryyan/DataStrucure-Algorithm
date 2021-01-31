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


# C Implementation

# void wcReverseString( wchar_t str[], int start, int end ){
#   wchar_t temp;
#   while ( end > start ){
# /* Exchange characters */
#       temp = str[start];
#       str[start] = str[end];
#       str[end] = temp;
# /* Move indices towards middle */ start++; end--;
#   }
# }


# void wcReverseWords( wchar_t str[] ){
#   int start = 0, end = 0, length;
#   length = wcslen(str);
# /* Reverse entire string */
#   wcReverseString(str, start, length - 1);
#   while ( end < length ) {
#       if ( str[end] != L' ' ){ /* Skip non-word characters */ /* Save position of beginning of word */
#           start = end;
# /* Scan to next non-word character */
#           while ( end < length && str[end] != L' ' )
#               end++;
# /* Back up to end of word */
#           end--;
# /* Reverse word */
#           wcReverseString( str, start, end );
#       }
#       end++; /* Advance to next token */ }
# }
