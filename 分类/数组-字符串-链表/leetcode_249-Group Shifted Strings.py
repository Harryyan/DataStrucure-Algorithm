from collections import defaultdict

# We can shift a string by shifting each of its letters to its successive letter.

# For example, "abc" can be shifted to be "bcd".
# We can keep shifting the string to form a sequence.

# For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
# Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. 
# You may return the answer in any order.


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        records = defaultdict(list)
        for s in strings:
            records[self._hash(s)].append(s)

        return list(records.values())
            

    def _hash(self,s):
        return tuple((ord(s[i]) - ord(s[i-1])) % 26 for i in range(1,len(s)))


so = Solution()
strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

r = so.groupStrings(strings)
print(r)