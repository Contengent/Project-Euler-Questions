import time

startTime = time.time()


def hollowAtIndex(s, index):
    # Adjust index for reverse positioning (0 is last character)
    adjusted_index = len(s) - 1 - index

    if adjusted_index < 0 or adjusted_index >= len(s):
        # raise IndexError("Index out of range")
        return "-1"

    # Replace the character at the adjusted index
    new_string = s[:adjusted_index] + "*" + s[adjusted_index + 1:]
    return new_string


BIG_PRIMES_LIST = []
PRIMES_TO_CHECK = []

with open("bigPrimesList.txt", "r") as file:
    for line in file:
        BIG_PRIMES_LIST.append(line.strip())


with open("primesToCheck.txt", "r") as file:
    for line in file:
        PRIMES_TO_CHECK.append(line.strip())

toHollow = []
indexToHollow = 1
secondIndexToHollow = 3
thirdIndexToHollow = 5
hollowedNumbers = []

# check these indecies:
# [100000] -> {



for number in PRIMES_TO_CHECK:
    temp_hollowed = (hollowAtIndex(str(number), indexToHollow))
    temp_hollowed = (hollowAtIndex(str(temp_hollowed), secondIndexToHollow))
    temp_hollowed = (hollowAtIndex(str(temp_hollowed), thirdIndexToHollow))
    if temp_hollowed not in hollowedNumbers:
        hollowedNumbers.append(temp_hollowed)

print(hollowedNumbers)

print("pre-hollow:  " + str(len(PRIMES_TO_CHECK)))

print("after hollow: " + str(len(hollowedNumbers)))

for house in hollowedNumbers:
    familyCount = 0
    for family_memeber in range(10):
        if str(str(house).replace("*", str(family_memeber))) in BIG_PRIMES_LIST:
            familyCount += 1

    if familyCount > 6:
        print("Found > 6: " + house)
        print("has: " + str(familyCount))

print("--- Done in:  %s seconds ---" % (time.time() - startTime))
print(":3")