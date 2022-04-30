def countIncreased(list):
    cont_increase = 0
    i = 0
    j = 0

    while i < len(list) -1:
        j = i + 1
        
        if list[j] > list[i]:
            cont_increase += 1
            
        i += 1

    return cont_increase   

def convertList(list):
    newList = []
    i = 0
    while i < len(list) -2:
        sum = list[i] + list[i+1] + list[i+2]
        newList.append(sum)
        i+=1
    return newList

def main():

  

    f = open("input.txt", "r")
    list = []
    for x in f:
        list.append(int(x))


    cont_increase = countIncreased(convertList(list))  
        
    print (cont_increase)


if __name__=='__main__':
  main()
