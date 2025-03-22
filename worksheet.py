matrix = [[2,4,1],
          [5,3,2],
          [2,6,8],
          [7,3,5],]

def check(matrix, target):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != target:
                print ('Row '+ str(row + 1) + ', Column ' + str(col + 1) + ' is not ' + str(target))
            else:
                print ('Row '+ str(row + 1) + ', Column ' + str(col + 1) + ' is ' + str(target))
                return



check(matrix,4)