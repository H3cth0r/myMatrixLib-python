# By Héctor Miranda García
# CALCULATION FUNCTIONS
from math import radians, sin, cos, pi
def matrixAddition(matrix_one, matrix_two): # Matrixes args as Lists
    """
    This function lets you make a matrix addition.
    
    Parameters:
        matrix_one : matrix as an array
        matrix_two : matrix as an array

    Return: 
        matrix : returns an array matrix
    """
    matrix = []
    if (len(matrix_one) == len(matrix_two)) and (len(matrix_one[0]) == len(matrix_two[0])):
        for i in range(len(matrix_one)):
            row = []
            for j in range(len(matrix_two[i])):
                row.append(matrix_one[i][j] + matrix_two[i][j])
            matrix.append(row)
    return matrix
def matrixSubstraction(matrix_one, matrix_two): # Matrixes args as Lists
    """
    This function lets you make a matrix substraction.

    Parameters:
        matrix_one : matrix as an array
        matrix_two : matrix as an array
    
    Return:
        Matrix : return an array matrix
    """
    matrix = []
    if (len(matrix_one) == len(matrix_two)) and (len(matrix_one[0]) == len(matrix_two[0])):
        for i in range(len(matrix_one)):
            row = []
            for j in range(len(matrix_two[i])):
                row.append(matrix_one[i][j] - matrix_two[i][j])
            matrix.append(row)
    return matrix
def matrixScalarProduct(scalar, matrix_one): # Matrixes args as Lists
    """
    This function lets you make a matrix scalar product operation:

    Parameters:
        scalar : float or integer
        matrix_one : matrix as an array

    Return:
        Matrix : as an array 
    """
    matrix = []
    for i in range(len(matrix_one)):
        row = []
        for j in range(len(matrix_one[i])):
            row.append(matrix_one[i][j] * scalar)
        matrix.append(row)
    return matrix    
def matrixProduct(matrix_one, matrix_two): # Matrixes args as objects
    """
    This function lets you make matrix product operation.

    Parameters:
        matrix_one : matrix as an array
        matrix_two : matrix as an array
    
    Return:
        Matrix as an array
    """
    if len(matrix_one[0]) == len(matrix_two):
        matrix = []
        for i in matrix_one:
            row = []
            for j in zip(*matrix_two):
                adds = 0
                for a, b in zip(i, j):
                    adds += a*b
                row.append(adds)
            matrix.append(row)
        return matrix
    else:
        return None
def matrixTranspons(matrix_one): # Matrix arg as List of the matrix
    matrix = []
    for i in range(len(matrix_one[0])):
        row = []
        for j in range(len(matrix_one)):
            row.append(matrix_one[j][i])
        matrix.append(row)
    return matrix
def delRowCol(matrixList, x, y):
    rows = len(matrixList)
    columns = len(matrixList[0])
    result = []
    for i in range(rows):
        row_result = []
        if i != x:
            for j in range(columns):
                if j != y:
                    row_result.append(matrixList[i][j])
            result.append(row_result)
    return result
def matrixMinor(matrixList, x, y): # Matrix arg as List of the matrix
    matrix = delRowCol(matrixList, x, y)
    return matrixDeterminant(matrix)
def matrixDeterminant(matrixList):# Matrix arg as List of the matrix
    if len(matrixList) == len(matrixList[0]):
        if len(matrixList) == 2:
            determinant = (matrixList[0][0]*matrixList[1][1]) - (matrixList[0][1]* matrixList[1][0])
            return determinant
        else:
            determinant = 0
            for i in range(len(matrixList)):
                co = matrixList[0][i]
                if i % 2 == 1:
                    co *= -1
                determinant += co * matrixMinor(matrixList, 0, i)
            return determinant
def matrixInverse(matrixList): # Matrix arg as List of the matrix
    if len(matrixList) == len(matrixList[0]):
        determinant = matrixDeterminant(matrixList)
        co_facts = []
        for i in range(len(matrixList)):
            co_facts_row = []
            for j in range(len(matrixList)):
                co = -1 if (i % 2) ^ (j % 2) else 1
                co_facts_row.append(co*matrixMinor(matrixList, i, j))
            co_facts.append(co_facts_row)
        inverse = []
        for i in matrixTranspons(co_facts):
            inv_row = []
            for j in i:
                inv_row.append(j / determinant)
            inverse.append(inv_row)
        return inverse
def showMatrix(matrix_list):
    for i in matrix_list:
        print("\t", i)
def matrix_rotation(point, theta):
    theta = radians(theta)
    matrix = [[1, 0, 0],[0, cos(theta), -sin(theta)],[0, sin(theta), cos(theta)]]
    return matrixProduct(matrix, point)
def point_generation(function, x0, xn, xdata, ydata, zdata, theta=5):
    for x in range(x0*10, xn*10, 1):
        x = x/10
        p = [[x], [function(x)], [0]]
        for angle in range(0, 360, theta):
            q = matrix_rotation(p, angle)
            xdata.append(q[0][0])
            ydata.append(q[1][0])
            zdata.append(q[2][0])
def calculate_volume(function, N):
    for n in range(1, N):
        volume = 0
        a = 1
        b = 4
        dx = (b-a)/n
        for i in range(n):
            xi = a + (dx*i)
            volume += function(xi)**2
        volume *= pi * dx
    return volume
class Matrix():
    def __init__(self, name, rows, columns, mlist=[]):
        self.matrix_name = name
        self.number_rows = rows
        self.number_columns = columns
        if mlist == []:
            self.matrix_list = self.generateMatrixList(self.number_rows, self.number_columns)
        else:
            self.matrix_list = mlist

    # SETTERS
    def setMatrixName(self, name):
        self.matrix_name = name
    def setNumberRows(self,rows):
        self.number_rows = rows  
    def setNumberColumns(self, columns):
        self.number_columns = columns
    def setMatrixList(self, ml):
        self.matrix_list = ml

    #  GETTERS
    def getMatrixName(self):
        return self.matrix_name
    def getNumberRows(self):
        return self.number_rows
    def getNumberColumns(self):
        return self.number_columns
    def getMatrixList(self):
        return self.matrix_list

    # CREATE MATRIX
    def generateMatrixList(self, rows, columns):
        matrix = []
        for i in range(rows):
            row = []
            for j in range(columns):
                row.append(int(input("row {}, column {}: ".format(i, j))))
            matrix.append(row)
        return matrix

    # PRINT MATRIX DATA
    def printMatrix(self):
        print("\t-> name : %s\n\t-> rows : %s\n\t-> columns : %s\n\t-> list : %s"%(self.matrix_name, self.number_rows, self.number_columns, self.matrix_list))
        print()
        for i in self.matrix_list:
            print("\t", i)
