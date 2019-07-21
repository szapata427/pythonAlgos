def add(n):
    string = str(n)
    total = 0
    for x in string:
        total += int(x)
    print(total)


add(29)

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

