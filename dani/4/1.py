

mBoard = [[] * 5 for i in range(5)]
mCall = [[] * 5 for i in range(5)]
def getNullCallBoard():
    mCall = [[] * 5 for i in range(5)]
    for i in range(5):
        mCall[i] = [False for i in range(5)]
    return mCall
        
def check(mCall, row, col):
    count = 0
    #check row
    for i in range(5):
        if mCall[row,i]:
            count +=1
    if count == 5 :
        return True
    count = 0
    #check col
    for i in range(5):
        if mCall[i,col]:
            count +=1
    if count == 5 :
        return True

    return False

def call(num, lBoard, lCall):
    for board in lBoard:
        #search the number
        


def main():

    file = open("input.txt","r")

    lcalled = file.readline().rstrip('\n').split(",")
    print(lcalled)
    lBoard = []
    lCall = []
 
    line = file.readline()                      #first time is \n
    while line != "":
        print("holas")
        mBoard = [[] * 5 for i in range(5)]
        for i in range(5):
            row = file.readline().rstrip('\n').split()
            mBoard[i]=row
        line = file.readline()
        lBoard.append(mBoard)
        lCall.append(getNullCallBoard())
        line = file.readline() 
    i = 0
    winner = []
    while winner == [] :
        winner = call(callNum, lBoard, lCall)
    
        

    


if __name__=='__main__':
  main()
