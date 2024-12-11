''' Obligitory timer '''
import time
start_time = time.time()


primeNumberCount = 1 # set to one because I wanted the while loop to look nice lol

verifiedPrimes = [2] # initialized with 2 bc duh
numberToCheck = 1
isCurrentPrime = False

while primeNumberCount < 10001:
    for prime in verifiedPrimes:
        if numberToCheck % prime != 0 and numberToCheck != 1:
            isCurrentPrime = True
        else:
            isCurrentPrime = False
            break


    if isCurrentPrime:
        print("prime found: ", numberToCheck)
        verifiedPrimes.append(numberToCheck)
        primeNumberCount += 1

    numberToCheck += 1


print(verifiedPrimes)
print(len(verifiedPrimes))
print("answer is: ", verifiedPrimes[(len(verifiedPrimes) - 1)])


print("--- Took %s seconds ---" % (time.time() - start_time)) # 3.8s on my vm, pretty slow but it was cool and I made it myself.
                                                              # I've been over using this method to solve questions involving primes lol
