def binaryToDecimal(b):
  
  i = 0
  l = len(b)
  d = 0
  
  while i < l :
    d += int(b[i]) * 2** (l-i-1)
    i+=1
  
  return d

def main():

  
  # common bit
  gamma = ''
  # no common bit
  epsilon = ''
  
  dictionary = []
  
  list = []

  f = open("input.txt", "r")
  for line in f:
    list.append(line)
  f.close()
  
  i = 0
  while i < len(list[1])-1:
    
    cont1 = 0
    cont0 = 0

    for line in list:
      if line[i] == '1':
        cont1 += 1
      else:
        cont0 += 1
    
    if cont1 > cont0:
      epsilon += "1"
      gamma += "0"
    else:
      epsilon += "0"
      gamma += "1"
    
    i += 1

  decimal_gamma =binaryToDecimal(gamma)
  decimal_epsion =binaryToDecimal(epsilon) 
  print(decimal_gamma * decimal_epsion)

if __name__=='__main__':
  main()

