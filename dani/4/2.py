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

def call(num, lBoard, lCall,lwinners):
    i = 0
    winner = []
    while i < len(lBoard) :
        board = lBoard[i]
        calls = lCall[i]
        #search the number
        if not lwinners[i]:
            for row in range(5):
                for col in range(5):
                    if board[row][col] == num:
                        calls[row][col] = True
                        if check(calls, row, col):
                            lwinners[i] =True
                            winner = [board,calls]
        i += 1
    return winner

def calculateScore(board, calls, lastCall):
    score= 0
    for row in range(5):
        for col in range(5):
            if not calls[row][col]:
                score += int(board[row][col])

        
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

    nBorads = len(lBoard)
    lwinners = [False for i in range(nBorads)]
    
    i = 0
    winner = []

    count =0
    lastScore = 0
    while i< len(lcalled)  and count !=100:
        result = call(lcalled[i], lBoard, lCall,lwinners)
        if result != [] :
            
            count += 1
            lastCall = lcalled[i]
            winner = result

            winnerBoard = winner[0]
            winnerCalls = winner[1]

            lastScore = calculateScore(winnerBoard,winnerCalls,lastCall)
            print(lastScore)
            result = []

        i+= 1
    print(winner)
    print(count)
    print(lwinners)
    
    print(i)
    winnerBoard = winner[0]
    winnerCalls = winner[1]
    print(lastCall)
    print(lastScore)
    

if __name__=='__main__':
  main()
