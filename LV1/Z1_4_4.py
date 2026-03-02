file = open("song.txt")

counter = {}

for line in file:
    for word in line.split():
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

file.close()

uniqueCounter = 0

for word, value in counter.items():
    if value == 1:
        print(word)
        uniqueCounter += 1

print("\nTotal unique words:", uniqueCounter)