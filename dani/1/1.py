file = open("input.txt","r")


prev = int(file.readline())

count = 0 
for n in file:
    num=int(n)
    if num > prev:
        count +=1
    prev = num

print(count) 
