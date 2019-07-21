def add(n):
    string = str(n)
    total = 0
    for x in string:
        total += int(x)
    print(total)


add(29)

matrix = [[1, 0, 0], 
          [0, 5, 0], 
          [0, 0, 3]]


def isDiagonalMatrix(matrix):
    rows = len(matrix)
    
    columns = rows
    print(columns)
    for x in matrix:
        print(len(x))
        print(x)
        if len(x) != rows:
            return False
    
    return True

