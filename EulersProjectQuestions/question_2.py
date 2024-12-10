import time
start_time = time.time()


# Fibonacci Sequence
current_number = 0
iterator = 0

tempFibonacchi_1 = 1
tempFibonacchi_2 = 0

fibonacchiSequence = [] #[1] too lazy to figure out how to get the first 1 in the sequence


while current_number < 4000000:
    current_number = tempFibonacchi_1 + tempFibonacchi_2
    tempFibonacchi_2 = tempFibonacchi_1
    tempFibonacchi_1 = current_number

    if current_number % 2 == 0:
        fibonacchiSequence.append(current_number)

#print("Sequence:",fibonacchiSequence)
#print("length:",len(fibonacchiSequence))

answer = 0

for number in fibonacchiSequence:
    answer += number
print("answer:", answer)

print("--- %s seconds ---" % (time.time() - start_time))