import datetime


def firstNonRepeated(str):
    charHash = {}

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
result = firstNonRepeated("我们我们😺")
end_time = datetime.datetime.now()

time_diff = (end_time - start_time).total_seconds() * 1000

print(str(time_diff) + " ms")
print(result)
