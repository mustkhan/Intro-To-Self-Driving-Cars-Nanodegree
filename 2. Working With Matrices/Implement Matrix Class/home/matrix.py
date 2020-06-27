import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

def dotproduct(vectora, vectorb):
    
    # variable for accumulating the sum
    result = 0
    
    # TODO: Use a for loop to multiply the two vectors
    # element by element. Accumulate the sum in the result variable
    count = 0
    for i in vectora:
        result = result + i*vectorb[count]
        count+=1
    return result

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
    
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here        
        if self.h == 1:
            determinantResult = self.g[0][0]
            return determinantResult
           
        if self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            determinantResult = a*d - b*c
            return determinantResult

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        else:
            total=0
            for i in range(len(self[0])):
                x=self[i][i]
                total = total + x
            return total

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        
        ## Check if matrix is 1x1 or 2x2.
        ## Depending on the matrix size, the formula for calculating
        ## the inverse is different. 
        
        
        if self.h == 1:
            inverseResult = zeroes(1,1)
            inverseResult[0][0] = 1/self.g[0][0]
            return inverseResult 

        # If the matrix is 2x2, check that the matrix is invertible

        if self.h == 2 and self.g[0][0]*self.g[1][1] != self.g[0][1]*self.g[1][0]:
            inverseResult = zeroes(2, 2)
            determinantResult = self.determinant()
            inverseResult[0][0] = self.g[1][1] * (1/determinantResult)
            inverseResult[0][1] = -self.g[0][1] * (1/determinantResult)
            inverseResult[1][0] = -self.g[1][0] * (1/determinantResult)
            inverseResult[1][1] = self.g[0][0] * (1/determinantResult)
            return inverseResult
        else:
            raise(ValueError, "Matrix is not invertible")
           
        
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        Transpose = zeroes(self.w,self.h)
        for j in range(self.w):
            for i in range(self.h):
                Transpose[j][i] = self.g[i][j]
        return Transpose

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        
        matrixAddition = zeroes(self.h,self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                matrixAddition[i][j] = self.g[i][j]+other.g[i][j]
        return matrixAddition

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        negativeMatrix = zeroes(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                negativeMatrix[i][j] = (-1 * self.g[i][j])
        return negativeMatrix

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        
        matrixSubtraction = zeroes(self.h,self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                matrixSubtraction[i][j] = self.g[i][j]-other.g[i][j]
        return matrixSubtraction

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #Check if matrix multiplication is not possible
        if self.w != other.h :
            raise(ValueError, "Matrices cannot be multiplied") 
        
        matrixMultiply = zeroes(self.h,other.w)
        otherTranspose = other.T()
        
        for i in range (self.h):
            for j in range (otherTranspose.h):
                matrixMultiply[i][j] = dotproduct(self.g[i],otherTranspose.g[j]) 
                #Note that dot product function seperately defined at the start of matrix.py file
        return matrixMultiply

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            rmulti = zeroes(self.h, self.w)
            for i in range(self.h):
                for j in range(self.w):
                    rmulti[i][j] = self.g[i][j] * other
            return rmulti