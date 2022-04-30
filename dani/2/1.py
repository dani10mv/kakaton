file = open("input.txt","r")

dep = 0
hor = 0

for line in file:
    sline =line.split()
    order =sline[0]
    num = int(sline[1])

    if order == "forward":
        hor +=num
    elif order == "down":
        dep += num
    else:
        dep -= num
print(hor * dep)
