
def binaryToDecimal(b):
    b = str(b)
    i = 0
    l = len(b)
    d = 0
    while i < l :
        d += int(b[i]) * 2** (l-i-1)
        i+=1
    return d

def getLeast(most):
    if most == 1:
        return 0
    else:
        return 1

def getMostCommonInPosition(list, i):
    count1 = 0
    count0 = 0
   
    for num in list:
       
        if num[i] == "1":
            count1 += 1
        else:
            count0 += 1

    if count1 >= count0 :
        return 1
    else:
        return 0

def getNumbresWithBitInPos(list, bit, pos):
    newList = []
    for num in list:
        if int(num[pos]) == bit:
            newList.append(num)
    return newList

def main():
        
    file = open("input.txt","r")

    

    list = []
    for line in file: 
        list.append(line.rstrip('\n'))
    
    oxList = list #mas comun
    ocList = list # menos comun

    i = 0
    
    
    while len(oxList) > 1 :
       
        
        oxList = getNumbresWithBitInPos(oxList, getMostCommonInPosition(oxList, i), i) 
        i+=1

    i=0
    while len(ocList) > 1 :
        
        ocList = getNumbresWithBitInPos(ocList, getLeast(getMostCommonInPosition(ocList, i)), i)
        i+=1


    print (oxList)
    print (ocList)
    oc = binaryToDecimal(ocList[0])
    ox = binaryToDecimal(oxList[0])
   
    print(ox * oc)

if __name__=='__main__':
  main()

