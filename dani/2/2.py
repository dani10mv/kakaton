file = open("input.txt","r")

dep = 0
hor = 0
aim = 0

for line in file:
    sline =line.split()
    order =sline[0]
    num = int(sline[1])

    if order == "forward":
        hor +=num
        dep += aim * num
    elif order == "down":
        aim += num
    else:
        aim -= num
        
print(hor * dep)
