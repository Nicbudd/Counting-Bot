file = open("primes.txt")

primes = []

for line in file:
    line = line.split(",")
    for item in line:
        print(item)
        if not item == "\n":
            primes.append(item)

file.close()

print(primes)

file = open("primesSorted.txt", "w")

for item in primes:
    file.write(item + "\n")

file.close()