# data setup
f = open("AdventOfCode-2024/day1/data.txt")
data = f.read()
# print(data)

data = data.split("\n")
right = []
left = []
for d in data:
    l,r = d.split("  ")
    right.append(int(r.strip()))
    left.append(int(l.strip()))
# data setup

rightMapOfFreq = {}
for r in right:
    if r in rightMapOfFreq:
        rightMapOfFreq[r]+=1
    else:
        rightMapOfFreq[r] = 1

print(rightMapOfFreq)

similarityScore = 0
for l in left:
    if l in rightMapOfFreq:
        similarityScore += (l*rightMapOfFreq[l])

print(similarityScore)
