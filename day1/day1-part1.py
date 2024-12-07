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


right.sort()
left.sort()

count = 0
for i in range(0,len(right)):
    count += abs(right[i]-left[i])

print(count)

