
def binaryToDecimal(b):
    i = 0
    l = len(b)
    d = 0
    while i < l :
        d += int(b[i]) * 2** (l-i-1)
        i+=1
    return d


def main():
        
    file = open("input.txt","r")

    gamma = "" #mas comun
    epsilon = "" # menos comun

    list = []
    for line in file: 
        list.append(line)

    i = 0

    while i < len(list[1])-1:
 
        count1=0
        count0=0
        for num in list:
            if num[i] == "1":
                count1 += 1
            else:
                count0 += 1
        
        if count1 > count0:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
        i += 1
    dgamma =binaryToDecimal(gamma)
    depsion =binaryToDecimal(epsilon) 
    print (gamma)
    print(epsilon)
    print(dgamma * depsion)

if __name__=='__main__':
  main()
