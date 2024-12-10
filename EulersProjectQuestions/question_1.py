multiples = []
sumOfAll = 0

for number in range(1,1000):
    if number%3 == 0 or number%5  == 0:
        if number not in multiples:
            multiples.append(number)

print(multiples)

for number in multiples:
    sumOfAll += number

print("Answer:", sumOfAll)