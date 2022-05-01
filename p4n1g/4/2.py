
def main():

  def matrix_win(matrix):
    cont_x_line = 0
    cont_x_col  = 0
    i = 0
    j = 0
    for i in range(5):
      cont_x_line = 0
      cont_x_col  = 0
      for j in range(5): 
        if matrix[i][j].find('X') > 0:
          cont_x_line += 1
        if matrix[j][i].find('X') > 0:
          cont_x_col += 1

      if cont_x_line == 5 or cont_x_col == 5:
        return 1
  

  def result(matrix, winner_n):
    i = 0
    j = 0
    cont_no_x = 0
    print('================\n')
    print('Winner with ' + str(winner_n))
    print('================\n')
    for i in range(5):
      for j in range(5):
        if not(matrix[i][j].find('X') > 0):
          cont_no_x = cont_no_x + int(matrix[i][j])
    
    result = cont_no_x * int(winner_n);
    return result


  mBoard = [[] * 5 for i in range(5)]
  lBoard = []
  wBoards = []

  # Get the winners numbers
  file = open("input.txt", "r")
  numbers = file.readline().rstrip('\n')

  winner_numbers = numbers.split(',')

  line = file.readline()                      #first time is \n
  while line != "":
      mBoard = [[] * 5 for i in range(5)]
      for i in range(5):
          row = file.readline().rstrip('\n').split()
          mBoard[i]=row
      line = file.readline()
      lBoard.append(mBoard)
  
  print(winner_numbers)

  flag_winner = 0

  for winner in winner_numbers:
      print('************************')
      print('Ganador -> '+ winner + '\n')
      indice = len(lBoard) -1
      while indice >= 0:
        matrix = lBoard[indice]
        for i in range(5):
          for j in range(5):

              if winner == matrix[i][j]:
                matrix[i][j] = matrix[i][j] +'X'

                if matrix_win(matrix) == 1:
                  print('--------------------\n')
                  print(matrix)
                  print(result(matrix, winner))
                  
                  wBoards.append(matrix)
                  lBoard.remove(matrix)
                  
                  print('--------------------\n')
        indice -= 1
  
  print(len(wBoards))

if __name__=='__main__':
  main()

