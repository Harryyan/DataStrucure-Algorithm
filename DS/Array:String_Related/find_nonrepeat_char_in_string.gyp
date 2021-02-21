import datetime

# PROBLEM:
# Write an efficient function to find the first nonrepeated character in a string.
# For instance, the first nonrepeated character in “total” is ‘o’ and the first nonrepeated
# character in “teeter” is ‘r’. Discuss the efficiency of your algorithm.

# Solution:
# A hash table may be a better choice when str and remove are short or characters
# have many possible values (for example, Unicode strings).


def firstNonRepeated(str):
    charHash = {}

    # Build hashmapg
    for char in str:
        if char in charHash:
            charHash[char] += 1
        else:
            charHash[char] = 1

    # Find the 1st non-repeat character
    for key, value in charHash.items():
        if value == 1:
            return key

    return None


start_time = datetime.datetime.now()
result = firstNonRepeated("😂😂😊😊😜😜😙😙😝😝😺😝🤑😄🤣☺️😋😌😌🤓")
end_time = datetime.datetime.now()

time_diff = (end_time - start_time).total_seconds() * 1000

print(str(time_diff) + " ms")
print(result)
