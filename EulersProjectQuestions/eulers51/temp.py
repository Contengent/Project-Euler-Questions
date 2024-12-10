from main import BIG_PRIMES_LIST


def hollowAtIndex(s, index):
    # Adjust index for reverse positioning (0 is last character)
    adjusted_index = len(s) - 1 - index

    if adjusted_index < 0 or adjusted_index >= len(s):
        # raise IndexError("Index out of range")
        return "-1"

    # Replace the character at the adjusted index
    new_string = s[:adjusted_index] + "*" + s[adjusted_index + 1:]
    return new_string

def has_three_asterisks(input_string):
    """
    Check if the input string contains exactly three '*' characters.
    """
    count = input_string.count('*')  # Count the occurrences of '*'
    return count == 3


index1 = 1
index2 = 1
index3 = 1

possiblHollows = []
threeHollows = []
hollowThis = "999999"
tmpHollowed = "0"

for i in range(10):
    for j in range(10):
        for k in range(10):
            tmpHollowed = hollowAtIndex(hollowThis, k)
            tmpHollowed = hollowAtIndex(tmpHollowed, j)
            tmpHollowed = hollowAtIndex(tmpHollowed, i)

            if tmpHollowed not in possiblHollows:
                possiblHollows.append(tmpHollowed)

            tmpHollowed = "0"

            index3 += 1
        index2 += 1
    index1 += 1

for possibility in possiblHollows:
    if (has_three_asterisks(possibility)):
        threeHollows.append(possibility)

print(threeHollows)

# prime checker
BIG_PRIMES_LIST = []
toCheck = []
inNumber = "*2*3*3"


        #

with open("bigPrimesList.txt", "r") as file:
    for line in file:
        BIG_PRIMES_LIST.append(line.strip())


for i in range(10):
    tmp = str(inNumber.replace("*", str(i)))
    if tmp in BIG_PRIMES_LIST:
        print(tmp)



'''
[543210
'99***9', 
'9*9**9', 
'*99**9', 
'9**9*9', 
'*9*9*9', 
'**99*9', 
'9***99', 
'*9**99', 
'**9*99', 
'***999'
]
'''