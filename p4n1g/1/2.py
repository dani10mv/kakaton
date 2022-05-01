


def main():

  cont_increase = 0

  f = open("input.txt", "r")
  list = []
  for x in f:
    list.append(int(x))

  i = 0
  j = 0

  clean_list = []

  def sum(i, j, x):
    sum_ijx = list[i] + list[j] + list[x]
    return sum_ijx

  while i < len(list) -2:
      j = i + 1
      x = j + 1
      
      sum_ijx = sum(i, j, x)
      clean_list.append(sum_ijx)

      i += 1

  i = 0
  while i < len(clean_list) -1:
    j = i + 1
    
    if clean_list[j] > clean_list[i]:
        cont_increase += 1
        
    i += 1   

  print(cont_increase)

if __name__=='__main__':
  main()

