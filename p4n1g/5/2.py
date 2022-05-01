
from operator import truediv


def main():

  def lower(n1, n2):
    if n1 <= n2:
      return n1
    else:
      return n2

  dict = {}
  # create a dictionary with matrix n
  i = 0
  j = 0
  for i in range(1000):
    for j in range(1000):
      key = str(i)+','+str(j) 
      dict[key] = 0
  
  file = open("input.txt", "r")
  
  for line in file:
    line = line.rstrip('\n')
    line_array = line.split(' -> ')

    x1_y1 = line_array[0]
    x1_y1_array = x1_y1.split(',')
    x1 = int(x1_y1_array[0])
    y1 = int(x1_y1_array[1])

    x2_y2 = line_array[1]
    x2_y2_array = x2_y2.split(',')
    x2 = int(x2_y2_array[0])
    y2 = int(x2_y2_array[1])
  
    if x1 == x2:
      aux_y1 = int(y1)
      aux_y2 = int(y2)
      # OK
      if aux_y1 < aux_y2:
        while aux_y1 <= aux_y2:
          aux_key = str(x1)+','+str(aux_y1)
          dict[aux_key] += 1
          aux_y1 += 1
      # OK
      elif aux_y1 > aux_y2:
        while aux_y1 >= aux_y2:
          aux_key = str(x1)+','+str(aux_y1)
          dict[aux_key] += 1
          aux_y1 -= 1
    # OK
    elif y1 == y2:
      aux_x1 = int(x1)
      aux_x2 = int(x2)
      if aux_x1 < aux_x2:
        while aux_x1 <= aux_x2:
          aux_key = str(aux_x1)+','+str(y1)
          dict[aux_key] += 1
          aux_x1 += 1
      # OK
      elif aux_x1 > aux_x2:
        while aux_x1 >= aux_x2:
          aux_key = str(aux_x1)+','+str(y1)
          dict[aux_key] += 1
          aux_x1 -= 1
    
    else:
      aux_x1 = int(x1)
      aux_y1 = int(y1)
      aux_x2 = int(x2)
      aux_y2 = int(y2)
      if abs(aux_x1 - aux_x2) == abs(aux_y1 - aux_y2):
        # Tacho las puntas, y ahora los puntos intermedios
        aux_key_1 = str(x1)+','+str(y1)
        dict[aux_key_1] += 1
        aux_key_2 = str(x2)+','+str(y2)
        dict[aux_key_2] += 1

        if aux_x1 >= aux_x2:
          aux_extra = lower(aux_y1, aux_y2)
          while aux_x1 > aux_x2:
            aux_x1 -= 1
            aux_extra += 1
            aux_key = str(aux_x1)+','+str(aux_y1)
            dict[aux_key] += 1
        # OK
        elif aux_x1 < aux_x2:
          aux_extra = lower(aux_y1, aux_y2)
          while aux_x1 <= aux_x2:
            aux_x1 += 1
            aux_extra -= 1
            aux_key = str(aux_x1)+','+str(aux_y2)
            dict[aux_key] += 1
            
  contador = 0
  i = 0
  j = 0
  for i in range(1000):
    for j in range(1000):
      key = str(i)+','+str(j) 
      if dict[key] > 1:
        contador += 1
  print(contador)

if __name__=='__main__':
  main()

