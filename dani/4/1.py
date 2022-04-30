
def getNullCallBoard():
    mCall = [[] * 5 for i in range(5)]
    for i in range(5):
        mCall[i] = [False for i in range(5)]
    return mCall
        
def check(mCall, row, col):
    count = 0
    #check row
    for i in range(5):
        if mCall[row][i]:
            count +=1
    if count == 5 :
        return True
    count = 0
    #check col
    for i in range(5):
        if mCall[i][col]:
            count +=1
    if count == 5 :
        return True

    return False

def call(num, lBoard, lCall):
    i = 0
    while i < len(lBoard):
        board = lBoard[i]
        calls = lCall[i]

        #search the number
        for row in range(5):
            for col in range(5):
                if board[row][col] == num:
                    calls[row][col] = True
                    if check(calls, row, col):
                        return [board,calls]
        i += 1
    return []

def calculateScore(board, calls, lastCall):
    score= 0
    for row in range(5):
        for col in range(5):
            if not calls[row][col]:
                score += int(board[row][col])
    print (score)
    return score * int(lastCall)



def main():

    file = open("input.txt","r")

    lcalled = file.readline().rstrip('\n').split(",")
    lBoard = []
    lCall = []
 
    line = file.readline()                      #first time is \n
    
    while line != "":
      
        mBoard = [[] * 5 for i in range(5)]
        for i in range(5):
            row = file.readline().rstrip('\n').split()
            mBoard[i]=row
        lBoard.append(mBoard)
        lCall.append(getNullCallBoard())
        line = file.readline() 
        


    i = 0
    winner = []
    found = False
    
    while i< len(lcalled) and not found :
        result = call(lcalled[i], lBoard, lCall)
        if result != [] :
            lastCall = lcalled[i]
            winner = result
            print(lastCall)
            print(result)
            found = True
        i+= 1

    winnerBoard = winner[0]
    winnerCalls = winner[1]
    
    print(calculateScore(winnerBoard,winnerCalls,lastCall))
    
        

    


if __name__=='__main__':
  main()
