


def main():

  cont_increase = 0

  f = open("input.txt", "r")
  list = []
  for x in f:
    list.append(int(x))

  i = 0
  j = 0

  while i < len(list) -1:
      j = i + 1
      
      if list[j] > list[i]:
          cont_increase += 1
          
      i += 1

  print (cont_increase)   


if __name__=='__main__':
  main()

