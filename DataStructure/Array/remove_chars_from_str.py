# PROBLEM:
# Write an efficient function that deletes characters from a
# mutable ASCII string. Your function should take two arguments, str and remove.
# Any character existing in remove must be deleted from str. For example, given
# a str of "Battle of the Vowels: Hawaii vs. Grozny" and a remove of "aeiou",
# the function should transform str to "Bttl f th Vwls: Hw vs. Grzny".
# Justify any design decisions you make, and discuss the efficiency of your solution.

# Solution:


def removeChars(str, remove):
    strArray = list(str)
    char_flags = {}
    src = dst = 0

    for r in remove:
        char_flags[r] = True

    for s in strArray:
        char = strArray[src]
        if char_flags.get(char) != True:
            strArray[dst] = char
            dst += 1
        src += 1

    result = strArray[0:dst]
    return ''.join(result)


result = removeChars("Battle of the Vowels: Hawaii vs. Grozny", "aeiou")

print(result)


######## Java ########

# public static void removeChars( StringBuilder str, String remove ) {

#     boolean[] flags = new boolean['z' + 1]; // assumes ASCII, 123
#     int src, dst = 0;
#     // Set flags for characters to be removed
#     for (char c: remove.toCharArray()) {
#       flags[c] = true;
#     }
#
#     // Now loop through all the characters,
#     // copying only if they aren't flagged
#     for ( src = 0; src < str.length(); ++src ) {
#         char c = str.charAt(src); if ( !flags[ c ] ) {
#         str.setCharAt( dst++, c ); }
#     }
#     str.setLength(dst);
#     return;

# }
