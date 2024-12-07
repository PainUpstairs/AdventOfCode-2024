# data setup
f = open("AdventOfCode-2024/day2/data.txt")
data = f.read()
# print(data)

reports = []
for report in data.split("\n"):
    reports.append([int(r.strip()) for r in report.split(" ")])
# print(reports)
# data setup
def checkIfIncLevel(report, reverse):
    if reverse:
        report = reversed(report)

    up = -1
    sup = -1
    oneErr = False
    for lvl in report:
        print("up->",up)
        print("sup->",sup)
        if up < lvl:
            diff = abs(lvl-up)
            if (sup != -1 or up != -1) and (diff<1 or 3 <diff):
                    if oneErr == True:
                        return False
                    oneErr = True
                    continue
            sup = up
            up = lvl
        elif up == lvl:
            if oneErr == True:
                return False
            oneErr = True
        elif sup < lvl and lvl<up:
            if oneErr == True:
                return False
            oneErr = True
            up = lvl
        elif sup <= lvl:
            if oneErr == True:
                return False
            oneErr = True
    return True



safeCount  = 0
print(checkIfIncLevel([23,27,28,31,34,37,39,42],reverse=False))

# for report in reports:
#     if checkIfIncLevel(report, reverse=True):
#         safeCount+=1
#         print("inc -> ",report)
#     elif checkIfIncLevel(report,reverse=False):
#         print("dec -> ",report)
#         safeCount+=1
    # else :
    #     print


print(safeCount)




