# data setup
f = open("AdventOfCode-2024/day2/data.txt")
data = f.read()
# print(data)

reports = []
for report in data.split("\n"):
    reports.append([int(r.strip()) for r in report.split(" ")])
# print(reports)
# data setup


def checkIfValidLevel(level):
    lvlType = None
    for i in range(1,len(level)):
        diff = level[i-1]-level[i]
        if lvlType == None:
            # false => desc | true => inc
            lvlType = False if diff<0 else True
        if 3 < abs(diff) or ((lvlType == True and diff <= 0) or (lvlType == False and 0 <= diff)):
            return False
    return True

safeCount  = 0 
for report in reports:
    if checkIfValidLevel(report):
        print(report)
        safeCount+=1

print(safeCount)