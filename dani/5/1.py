def resize(matrix, size, newSize):
    newMatrix = matrix
    for i in range(newSize-size):
        newMatrix.append([0]*newSize)
    for i in range(size):
        for j in range(newSize-size):
            newMatrix[i].append(0)
    return newMatrix

def getRoutePoints(start, end, direction):

    list = []
    if direction == 0 : #horizontal
        for i in range(int(start[1]), int(end[1])+1):
            p = [int(start[0]), i ]
            list.append(p)
    elif direction == 1 : #vertical
        for i in range(int(start[0]), int(end[0])+1):
            p = [ i, int(start[1]) ]
            list.append(p)
    else : #diagonal
        y = int(start[1])
        increase = 1
        if int(start[0]) > int(end[0]):
            increase = -1
        
        for x in range(int(start[0]), int(end[0])+increase ,increase):
            
            p = [x,y]
            list.append(p)
            y += 1

    return list

def isDiagonal(pfrom,pto):
    
    dif0 = int(pfrom[0]) - int(pto[0])
    dif1 = int(pfrom[1]) - int(pto[1])
    if dif0 < 0:
        dif0 *= -1
    if dif1 < 0:
        dif1 *= -1
    if dif0 == dif1: 
        return True
        
    else:
        return False

def fillMatrix(matrix, pfrom, pto):

    horizontal = False
    start = pfrom
    end = pto
    count = 0
    direction =0

    if pfrom[0] == pto[0]:
        horizontal = True
    
    if horizontal:
        if int(pfrom[1]) > int(pto[1]):
            start = pto
            end = pfrom
        
    elif pfrom[1] == pto[1]:  #vertical
        if int(pfrom[0]) > int(pto[0]):
            start = pto
            end = pfrom
        direction =1
    else :
        if int(pfrom[1]) > int(pto[1]):
            start = pto
            end = pfrom
            
        direction =2
    routePoints = getRoutePoints(start, end, direction)

    for p in routePoints:

        matrix[p[0]][p[1]] +=  1
        if matrix[p[0]][p[1]] == 2:
            count += 1
    return count


def main():

    file = open("input.txt","r")

    lines = []
    for line in file: 
        lines.append(line.rstrip('\n'))

    size = 0
    matrix = []



    pointsCount = 0

    for line in lines:
        sline = line.split()
        pfrom = sline[0].split(',')
        pto = sline[2].split(',')
        
        max = size 
       
        if(int(pfrom[0])+1 > max):
            max = int(pfrom[0])+1
        if(int(pfrom[1])+1 > max):
            max = int(pfrom[1])+1
        if(int(pto[0])+1 > max):
            max = int(pto[0])+1
        if(int(pto[1])+1 > max):
            max = int(pto[1])+1
        if size < max:
            matrix = resize(matrix, size, max)
            size = max
        
     
        if pfrom[0] == pto[0] or pfrom[1] == pto[1] or isDiagonal(pfrom, pto):
            pointsCount += fillMatrix(matrix, pfrom, pto)
    print( pointsCount)


if __name__=='__main__':
  main()
