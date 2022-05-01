

def main():

  # forward add to horizontal
  horizontal = 0

  # up decreases to depth
  # down adds to depth
  depth = 0
  aim = 0

  f = open("input.txt", "r")

  n_aux = 0
  str_aux = []

  for x in f:
    str_aux = x.split()

    if str_aux[0] == 'forward':
      horizontal = horizontal + int(str_aux[1])
      depth = depth + (aim * int(str_aux[1]))

    elif str_aux[0] =='up':
      aim = aim - int(str_aux[1])

    elif str_aux[0] == 'down':
      aim = aim + int(str_aux[1])
      #depth = depth + int(str_aux[1])

  
  pow = horizontal * depth
  print(pow)

if __name__=='__main__':
  main()

