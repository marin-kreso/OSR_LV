file = open("SMSSpamCollection.txt")

hamCount = 0
spamCount = 0
hamWords = 0
spamWords = 0
spamQuestionMark = 0

for line in file:
    line = line.rstrip()

    if line.startswith("ham"):
        hamCount += 1
        hamWords += len(line.split()) - 1

    elif line.startswith("spam"):
        spamCount += 1
        spamWords += len(line.split()) - 1

        if line.endswith("?"):
            spamQuestionMark += 1

file.close()

print("Average ham words:", hamWords / hamCount)
print("Average spam words:", spamWords / spamCount)
print("Spam messages ending with '?':", spamQuestionMark)