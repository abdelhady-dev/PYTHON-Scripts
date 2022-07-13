# by : Abdelhady Saeed
# python 3.9

# global variable
num = int (input ('Enter the number of rows and columns in the square matrix : '))
arr = []

# functions
# difference between the sum of diagonal
def differenceSumDiagonal(array, num):
    diagonal1 = 0
    diagonal2 = 0
  
    for i in range(0, num):
      
        for j in range(0, num):
            # sum of frist diagonal
            if (i == j):
                diagonal1 += arr[i][j]
            # sum of second diagonal
            if (i == num - j - 1):
                diagonal2 += arr[i][j]
    return abs(diagonal1 - diagonal2)

# get the matrix from user
print('Enter the square matrix : ')
['1', '2', '3']
for i in range(0, num):
    try:
        line = input().split(' ')
        line = [int(item) for item in line]
        arr.append(line)
    except:
        print('You Enter a wrong value.')


# print the result
try:
    print ( 'The absolute difference between the sums of the matrix’s two diagonals = ', differenceSumDiagonal(arr, num))
except:
    print(' please try again.')